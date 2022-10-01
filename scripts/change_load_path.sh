#!/bin/sh

apk add bash

export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
poetry config virtualenvs.in-project true

cd /app/

poetry run python scripts/replace_load_path.py
