libgdx-updater
==============

Libgdx Library Updater

--------------
A command line Python script for updating all your libgdx libraries inside your project/workspace directory

Does not require eclipse, it finds your library files by itself, checks the nightlies server for the latest nightly, and updates your files.

With command line arguments you can update with a specific zip file.

#How to Use?
Either run the script with python in your project/workspace directory, or to specify a directory:
```
$ python libgdx-updater.py -d <YOUR_PROJECT_DIRECTORY>
```
You may also specify an archive to update from with:
```
$ python libgdx-updater.py -a <PATH_TO_ARCHIVE>
```
run the script with -h to see more options

---------------
#Example Usage:
```
jrenner@main:~/projects/missile$ cp ../libgdx_updater/libgdx_update.py .
jrenner@main:~/projects/missile$ python libgdx_update.py 
finding local libraries in /home/jrenner/projects/missile
found CORE libraries
found libraries for platform: ANDROID
found libraries for platform: DESKTOP
checking latest nightly...
-- OK --
lastest nightly from server: 2013-06-22 03:45:00
replace local libraries with files from latest nightly?(Y/n): y
downloading file: http://libgdx.badlogicgames.com/nightlies/libgdx-nightly-latest.zip
progress:         46.46 / 46.46 mB (100% complete)finished download
---------- CORE ----------
extracted to /home/jrenner/projects/missile/main/libs/gdx.jar
---------- DESKTOP ----------
extracted to /home/jrenner/projects/missile/desktop/libs/gdx-backend-lwjgl.jar
extracted to /home/jrenner/projects/missile/desktop/libs/gdx-backend-lwjgl-natives.jar
extracted to /home/jrenner/projects/missile/desktop/libs/gdx-natives.jar
---------- ANDROID ----------
extracted to /home/jrenner/projects/missile/android/libs/gdx-backend-android.jar
extracted to /home/jrenner/projects/missile/android/libs/armeabi/libgdx.so
extracted to /home/jrenner/projects/missile/android/libs/armeabi/libandroidgl20.so
extracted to /home/jrenner/projects/missile/android/libs/armeabi-v7a/libgdx.so
extracted to /home/jrenner/projects/missile/android/libs/armeabi-v7a/libandroidgl20.so
finished updates (815.68 seconds)
```


License is MIT License