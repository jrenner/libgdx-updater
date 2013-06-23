libgdx-updater
==============

Libgdx Library Updater

--------------
A command line Python script for updating all your libgdx libraries inside your project/workspace directory

Does not require eclipse, it finds your library files by itself, checks the nightlies server for the latest nightly, and updates your files.

With command line arguments you can update with a specific zip file.

Example Usage:
```
jrenner@main:~/projects/libgdx_updater$ python libgdx_update.py -d /home/jrenner/projects/missile
finding local libraries in /home/jrenner/projects/missile
location of gdx-backend-lwjgl.jar -> /home/jrenner/projects/missile/desktop/libs
location of gdx-backend-lwjgl-natives.jar -> /home/jrenner/projects/missile/desktop/libs
location of armeabi/libandroidgl20.so -> /home/jrenner/projects/missile/android/libs/armeabi
location of gdx-sources.jar -> /home/jrenner/projects/missile/main/libs
location of gdx.jar -> /home/jrenner/projects/missile/main/libs
location of armeabi-v7a/libandroidgl20.so -> /home/jrenner/projects/missile/android/libs/armeabi-v7a
location of gdx-natives.jar -> /home/jrenner/projects/missile/desktop/libs
location of gdx-backend-android.jar -> /home/jrenner/projects/missile/android/libs
location of armeabi-v7a/libgdx.so -> /home/jrenner/projects/missile/android/libs/armeabi-v7a
location of armeabi/libgdx.so -> /home/jrenner/projects/missile/android/libs/armeabi
checking latest nightly...
-- OK --
lastest nightly from server: 2013-06-22 03:45:00
replace local libraries with files from latest nightly?(Y/n): 
downloading file: http://libgdx.badlogicgames.com/nightlies/libgdx-nightly-latest.zip
progress:         46.46 / 46.46 mB (100%% complete)finished download
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
```


License is MIT License