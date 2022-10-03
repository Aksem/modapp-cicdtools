#!/bin/sh

poetry config virtualenvs.in-project true

cd /app/

LINUX_APPIMAGE_PATH=./buildtools_Linux/modapp_buildtools/resources/linux_appimage

echo "Create venv"
sh $LINUX_APPIMAGE_PATH/create_venv.sh

echo "Change load path"
sh $LINUX_APPIMAGE_PATH/change_load_path.sh

poetry run python -m nuitka \
            --standalone \
            --follow-imports \
            --assume-yes-for-downloads \
            --plugin-enable="pylint-warnings" \
            --warn-unusual-code \
            --warn-implicit-exceptions \
            --show-memory \
            --show-modules \
            modapp_cicdtools/cli.py
