#!/bin/sh

# $1 .. app name
# $2 .. app version

cp -R /app/scripts/squashfs-root/usr/** /usr/

export VERSION=$2

appimagetool -s deploy /app/$1_AppImage/usr/share/applications/$1.desktop
appimagetool /app/$1_AppImage/
