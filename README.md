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
jrenner@pc:~/tac$ libgdx-updater 
finding local libraries in /home/jrenner/projects/tac
WARNING - did not find the following:
	armeabi-v7a/libgdx-box2d.so not found
	x86/libgdx-box2d.so not found
	gdx-box2d-natives.jar not found
	armeabi/libgdx-box2d.so not found
	gdx-box2d.jar not found
	ios/libObjectAL.a not found
	gdx-backend-gwt.jar not found
	x86/libgdx.so not found
	sources/gdx-bullet-sources.jar not found
	ios/libdgx-bullet.a not found
	ios/libgdx-box2d.a not found
	gdx-box2d-sources.jar not found
	x86/libgdx-bullet.so not found
	ios/libgdx.a not found
	armeabi-v7a/libgdx-bullet.so not found
	gdx-box2d-gwt.jar not found
	armeabi/libgdx-bullet.so not found
	gdx-backend-robovm.jar not found
	gdx-box2d-gwt-sources.jar not found
found gdx-sources.jar -> /home/jrenner/projects/tac/main/libs
found gdx-bullet-natives.jar -> /home/jrenner/projects/tac/desktop/libs
found gdx-natives.jar -> /home/jrenner/projects/tac/desktop/libs
found gdx-backend-android.jar -> /home/jrenner/projects/tac/android/libs
found gdx-backend-lwjgl.jar -> /home/jrenner/projects/tac/desktop/libs
found gdx.jar -> /home/jrenner/projects/tac/main/libs
found gdx-bullet.jar -> /home/jrenner/projects/tac/main/libs
found armeabi-v7a/libgdx.so -> /home/jrenner/projects/tac/android/libs/armeabi-v7a
found gdx-backend-lwjgl-natives.jar -> /home/jrenner/projects/tac/desktop/libs
found armeabi/libgdx.so -> /home/jrenner/projects/tac/android/libs/armeabi
found CORE libraries
found libraries for platform: ANDROID
found libraries for platform: DESKTOP
found libraries for platform: BULLET
checking latest nightly...
-- OK --
lastest nightly from server: 2014-07-10 21:56:00
replace local libraries with files from latest nightly?(Y/n): Y
downloading file: http://libgdx.badlogicgames.com/nightlies/libgdx-nightly-latest.zip
progress:         42.50 / 42.50 MB (100% complete)
finished download
---------- CORE ----------
extracted to /home/jrenner/projects/tac/main/libs/gdx.jar
extracted to /home/jrenner/projects/tac/main/libs/gdx-sources.jar
---------- DESKTOP ----------
extracted to /home/jrenner/projects/tac/desktop/libs/gdx-backend-lwjgl.jar
extracted to /home/jrenner/projects/tac/desktop/libs/gdx-backend-lwjgl-natives.jar
extracted to /home/jrenner/projects/tac/desktop/libs/gdx-natives.jar
---------- ANDROID ----------
extracted to /home/jrenner/projects/tac/android/libs/gdx-backend-android.jar
extracted to /home/jrenner/projects/tac/android/libs/armeabi/libgdx.so
extracted to /home/jrenner/projects/tac/android/libs/armeabi-v7a/libgdx.so
---------- EXTENSION: BULLET ----------
extracted to /home/jrenner/projects/tac/main/libs/gdx-bullet.jar
extracted to /home/jrenner/projects/tac/desktop/libs/gdx-bullet-natives.jar
finished updates in 1m 39.8s

```


License is MIT License
