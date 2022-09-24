#!/bin/sh

cp -R /app/scripts/squashfs-root/usr/** /usr/
appimagetool -s deploy app/usr/share/applications/app.desktop
appimagetool app

