#!/bin/sh

cp -R /app/scripts/squashfs-root/usr/** /usr/
echo $1
ls /app/$1_AppImage/usr/share/applications/
appimagetool -s deploy /app/$1_AppImage/usr/share/applications/$1.desktop
appimagetool /app/$1_AppImage/
