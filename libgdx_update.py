#!/usr/bin/python
__appname__ = 'libgdx_library_updater'
__version__ = "0.1"
__author__ = "Jon Renner <rennerjc@gmail.com>"
__url__ = "http://www.github.com/jrenner/I_HAVEN'T_SET_THIS_YET_I_HOPE_YOU_DON'T_SEE_THIS"
__licence__ = "MIT"

import os, time, sys, urllib2, re, datetime, tempfile, zipfile, argparse

def fatal_error(msg):
    print "ERROR: %s" % msg
    sys.exit(1)

def warning_error(msg):
    print "WARNING: %s" % msg
    if not FORCE:
        answer = raw_input("abort? (Y/n): ")
        if answer in YES:
            fatal_error("USER QUIT")            

# constants

YES = ['y', 'ye', 'yes', '']
DATE_RE = r"[0-9]{1,2}-[A-Za-z]{3,4}-[0-9]{4}\s[0-9]+:[0-9]+"
REMOTE_DATE_FORMAT = "%d-%b-%Y %H:%M"
NIGHTLY_URL = "http://libgdx.badlogicgames.com/nightlies/dist/"

CORE_LIBS = ["gdx.jar",
             "gdx-sources.jar"]

DESKTOP_LIBS = ["gdx-backend-lwjgl.jar",
                "gdx-backend-lwjgl-natives.jar",
                "gdx-natives.jar"] 

ANDROID_LIBS = ["gdx-backend-android.jar",
                "armeabi/libgdx.so",
                "armeabi/libandroidgl20.so",
                "armeabi-v7a/libgdx.so",
                "armeabi-v7a/libandroidgl20.so"]

# parse arguments
EPILOGUE_TEXT = "%s\n%s" % (__author__, __url__) + "\nUSE AT YOUR OWN RISK!"
parser = argparse.ArgumentParser(description='LibGDX Library Updater %s' % __version__, epilog=EPILOGUE_TEXT)
parser.add_argument('-d', '--directory', help='set the libgdx project/workspace directory', default=os.getcwd())
parser.add_argument('-i', '--interactive', action='store_true', help='ask for confirmation for every file', default=False)
parser.add_argument('-f', '--force-update', action='store_true', help='no confirmations, just update without checking nightly\'s datetime', default=False)
parser.add_argument('-a', '--archive', help='specify libgdx zip file to use for update', default=None)
args = parser.parse_args()
PROJECT_DIR = args.directory
INTERACTIVE = args.interactive
FORCE = args.force_update
ARCHIVE = args.archive

# mutually exclusive
if FORCE:
    INTERACTIVE = False

# check the time of the latest archive on the nightlies server
def get_remote_archive_mtime():
    index_page = urllib2.urlopen("http://libgdx.badlogicgames.com/nightlies/")
    contents = index_page.read()
    print "-- OK --"
    # regex for filename
    regex = r"libgdx-nightly-latest\.zip"
    # add regex for anything followed by the nighlty html time format
    regex += r".*%s" % DATE_RE
    try:
        result = re.findall(regex, contents)[0]
    except IndexError as e:
        print "REGEX ERROR: failed to find '%s' in:\n%s" % (regex, contents)
        fatal_error("regex failure to match")
    try:
        mtime = re.findall(DATE_RE, result)[0]
    except IndexError as e:
        print "REGEX ERROR: failed to find datetime in: %s" % result
        fatal_error("regex failure to match")
    dtime = datetime.datetime.strptime(mtime, REMOTE_DATE_FORMAT)
    return dtime

# downloads and returns a temporary file contained the latest nightly archive
def download_libgdx_zip():
    libgdx = tempfile.TemporaryFile()
    url = "http://libgdx.badlogicgames.com/nightlies/libgdx-nightly-latest.zip"
    # testing url - don't hammer badlogic server, host the file on localhost instead
    # url = "http://localhost/libgdx-nightly-latest.zip"
    resp = urllib2.urlopen(url)
    print "downloading file: %s" % url
    total_size = resp.info().getheader('Content-Length').strip()
    total_size = int(total_size)    
    # base 10 SI units - following Ubuntu policy because it makes sense - https://wiki.ubuntu.com/UnitsPolicy
    total_size_megabytes = total_size / 1000000.0
    bytes_read = 0
    chunk_size = 10000 # 10kB per chunk
    while True:        
        chunk = resp.read(chunk_size)
        libgdx.write(chunk)
        bytes_read += len(chunk)        
        bytes_read_megabytes = bytes_read / 1000000.0
        percent = (bytes_read / float(total_size)) * 100
        sys.stdout.write("\rprogress: {:>8}{:.2f} / {:.2f} mB ({:.0f}%% complete)".format(
            "", bytes_read_megabytes, total_size_megabytes, percent))
        sys.stdout.flush()
        if bytes_read >= total_size:
            print "finished download"
            break
    return libgdx

def update_files(libs, locations, archive):    
    for lib in libs:        
        if lib in archive.namelist():            
            if INTERACTIVE:
                answer = raw_input("overwrite %s? (Y/n): " % lib)
                if answer not in YES:                    
                    print "skipped: %s" % lib        
                    continue
            with archive.open(lib, "r") as fin:
                filename = os.path.basename(lib)
                final_path = os.path.join(locations[lib], filename)
                with open(final_path, "w") as fout:
                    fout.write(fin.read())                    
                print "extracted to %s" % final_path
        
def run_core(locations, archive):
    title("CORE")
    update_files(CORE_LIBS, locations, archive)

def run_android(locations, archive):
    title("ANDROID")
    update_files(ANDROID_LIBS, locations, archive)    

def run_desktop(locations, archive):
    title("DESKTOP")
    update_files(DESKTOP_LIBS, locations, archive)    


def search_for_lib_locations(directory):
    search_list = CORE_LIBS + DESKTOP_LIBS + ANDROID_LIBS
    locations = {}    
    for element in search_list:
        locations[element] = None
    for (this_dir, dirs, files) in os.walk(directory):        
        for element in search_list:
            split_path = os.path.split(element)
            path = os.path.split(split_path[0])[-1]
            filename = split_path[1]
            for f in files:
                match = False
                if filename == f:
                    f_dir = os.path.split(this_dir)[-1]                    
                    if path == "":
                        match = True
                    else:
                        if path == f_dir:
                            match = True
                if match:
                    if locations[element] != None:
                        print "WARNING: found %s in more than one place!" % element
                        if not FORCE:
                            answer = raw_input("continue? (Y/n): ")
                            if answer not in YES:
                                fatal_error("USER ABORT")
                    locations[element] = this_dir
    for lib, loc in locations.items():
        if loc == None:
            warning_error("WARNING: did not find library %s in this directory tree!\nchange current directory or project path as argument" % lib)
    return locations
        


def main():
    print "finding local libraries in %s" % PROJECT_DIR
    locations = search_for_lib_locations(PROJECT_DIR)

    for lib, loc in locations.items():
        print "location of %s -> %s" % (lib, loc)    
    if ARCHIVE == None:
        print "checking latest nightly..."
        mtime = get_remote_archive_mtime()
        print "lastest nightly from server: %s" % mtime
        if not FORCE:
            answer = raw_input("replace local libraries with files from latest nightly?(Y/n): ")    
            if answer not in YES:
                fatal_error("USER QUIT")
        libgdx = download_libgdx_zip()        
    else:
        if not os.path.exists(ARCHIVE):
            fatal_error("archive file not found: %s" % ARCHIVE)
        if not FORCE:
            answer = raw_input("replace local libraries with files from '%s'?(Y/n): " % os.path.basename(ARCHIVE))    
            if answer not in YES:
                fatal_error("USER QUIT")
        libgdx = open(ARCHIVE, "r")

    with zipfile.ZipFile(libgdx) as archive:        
        run_core(locations, archive)
        run_desktop(locations, archive)
        run_android(locations, archive)

    libgdx.close()

def title(text):
    dashes = "-" * 10
    print dashes + " %s " % text + dashes

if __name__ == "__main__":
    main()