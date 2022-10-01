#!/bin/sh

cd /app/

# BUILD_DEPS="build-base libffi-dev"
# # pyenv requires bash
# # nuitka standalone requires patchelf
# apk add $BUILD_DEPS bash patchelf
# ###############
# # Step 1: install dependencies
# ###############
# poetry config virtualenvs.in-project true
# poetry install #  -vvv
#
# cp -f ./.venv/lib/python3.10/site-packages/nuitka/build/static_src/MetaPathBasedLoader.c ./scripts/original_MetaPathBasedLoader.c
# cp -f ./scripts/MetaPathBasedLoader.c ./.venv/lib/python3.10/site-packages/nuitka/build/static_src/

# ##############
# Step 4: compile
# ##############
# export PYENV_ROOT="$HOME/.pyenv"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
# poetry run python -m nuitka \
#             --standalone \
#             --follow-imports \
#             --assume-yes-for-downloads \
#             --plugin-enable="pylint-warnings" \
#             --warn-unusual-code \
#             --warn-implicit-exceptions \
#             --show-memory \
#             --show-modules \
#             modapp_cicdtools/cli.py

###############
# Step 5: pre-deploy(create AppDir)
###############


###############
# Step 6: Deploy & Package(create AppImage)
###############
# Prepare go-appimage
# apk add file
cp -R scripts/squashfs-root/usr/** /usr/
appimagetool -s deploy app/usr/share/applications/app.desktop
appimagetool app

# apk del $BUILD_DEPS
