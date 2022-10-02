#/bin/sh

# export PYENV_ROOT="$HOME/.pyenv"
# eval "$(pyenv init -)"
# eval "$(pyenv virtualenv-init -)"
poetry config virtualenvs.in-project true

cd /app/

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
