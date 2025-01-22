[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name (doit être unique, utilisez un nom de domaine inversé)
package.name = org.test.myapp

# (str) Package domain (nécessaire pour Android/iOS)
package.domain = org.test

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
# Exemple : source.include_patterns = assets/*,images/*.png
source.include_patterns = assets/*,images/*

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# Ajoutez ici les dépendances nécessaires (par exemple, kivy)
requirements = python3,kivy

# (str) Presplash of the application (optionnel)
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application (optionnel)
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
# Options valides : landscape, portrait, portrait-reverse, landscape-reverse
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions (ajoutez les permissions nécessaires)
# Exemple : INTERNET, WRITE_EXTERNAL_STORAGE, etc.
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 33

# (str) Android NDK version to use
android.ndk = 25b

# (list) Android archs to build for
# Options : armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (str) Android entry point, default is ok for Kivy-based app
android.entrypoint = org.kivy.android.PythonActivity

# (str) Android app theme, default is ok for Kivy-based app
# android.apptheme = "@android:style/Theme.NoTitleBar"

# (bool) Enable AndroidX support (nécessaire pour certaines dépendances)
# android.enable_androidx = True

# (str) Logcat filters (pour afficher les logs Python)
android.logcat_filters = *:S python:D

# (bool) Allow backup (optionnel)
android.allow_backup = True

# (str) Release artifact format (apk or aab)
# android.release_artifact = apk

# (str) Debug artifact format (apk or aar)
# android.debug_artifact = apk

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .aab, .ipa) storage
bin_dir = ./bin
