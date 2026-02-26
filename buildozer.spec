[app]

title = Jarvis
package.name = jarvis
package.domain = org.jarvis.app

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android config
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# Permissions (add if needed)
android.permissions = INTERNET

# Architecture
android.arch = armeabi-v7a

# Log level
log_level = 2

# Exclude files
source.exclude_dirs = tests,bin,__pycache__

[buildozer]

log_level = 2
warn_on_root = 1
