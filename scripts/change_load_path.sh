#!/bin/sh

apk add bash

export PYENV_ROOT="$HOME/.pyenv"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
poetry config virtualenvs.in-project true

cd /app/

NUITKA_PATH=$(poetry run python -c "import nuitka; import os; print(os.path.dirname(nuitka.__file__))")
SOURCE_FILE="$NUITKA_PATH/build/static_src/MetaPathBasedLoader.c"

STRING_TO_REPLACE="        appendStringSafe(filename, getBinaryDirectoryHostEncoded(), sizeof(filename));"
NEW_STRING=$(cat <<-END
        appendStringSafe(filename, getBinaryDirectoryHostEncoded(), sizeof(filename));
        // new code
        appendCharSafe(filename, SEP, sizeof(filename));
        appendStringSafe(filename, "..", sizeof(filename));
        appendCharSafe(filename, SEP, sizeof(filename));
        appendStringSafe(filename, "usr", sizeof(filename));
        appendCharSafe(filename, SEP, sizeof(filename));
        appendStringSafe(filename, "lib", sizeof(filename));
        // new code end
END
)

# keep original copy
cp $SOURCE_FILE /app/

sed -i "s|$STRING_TO_REPLACE|$NEW_STRING|gi" $NUITKA_PATH/build/static_src/MetaPathBasedLoader.c
