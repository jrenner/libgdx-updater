##Libgdx Library Updater
=========================

This is a command line utility for updating the libgdx libraries inside your project's directory tree.
Although libgdx already has a GUI utility for updating libgdx libraries inside a project, it only works with Eclipse projects (to my knowledge).
(EDIT: Since this utility was created, libgdx has implemented gradle based build system that supports more than just Eclipse)
This python script works by walking through the directory tree and figuring out where you have stored the libraries, so it is IDE agnostic.
It does not depend on Eclipse, IntelliJ IDEA or any other project/workspace structure.
First it will check and download the latest nightly from the nightlies server, or use an archive you specify as a command line argument.
Then this archive will be used to update the libraries inside your project. 

====================
###Note:
Currently supports Android, Desktop, iOS (RoboVM) and GWT

Supported Extensions:
Box2D
Bullet

==================
###How to Use?
Either run the script with python in your project/workspace directory, or to specify a directory:
```
$ python libgdx-updater.py -d <YOUR_PROJECT_DIRECTORY>
```
You may also specify an archive to update from with:
```
$ python libgdx-updater.py -a <PATH_TO_ARCHIVE>
```
run the script with -h to see more options

=================
###Example Usage
(running in project directory)
```
jrenner@main:~/projects/missile$ python libgdx_update.py
finding local libraries in /home/jrenner/projects/missile
found CORE libraries
found libraries for platform: ANDROID
found libraries for platform: DESKTOP
WARNING: did not find libraries for platform: GWT - WILL NOT UPDATE
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
