#!/bin/sh

PYTHON_BUILD_DEPS="build-base libffi-dev openssl-dev bzip2-dev zlib-dev readline-dev sqlite-dev xz-dev"

apk add bash $PYTHON_BUILD_DEPS

export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
poetry config virtualenvs.in-project true

cd /app/
poetry install