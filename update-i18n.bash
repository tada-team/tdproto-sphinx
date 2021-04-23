#!/bin/bash
set -euo pipefail
shopt -s extdebug
IFS=$'\n\t'

BUILD_DIR="./build_gettext/"
RU_DIR="./docs/locale/ru/LC_MESSAGES"

sphinx-build -b gettext "./docs" "$BUILD_DIR"

for POT_FILE_PATH in "$BUILD_DIR"/*.pot; do
    POT_FILE_STEM=$(echo "$POT_FILE_PATH" | awk --field-separator='/' '{print $NF}' | cut --delimiter '.' --field 1)
    RU_PO_PATH="${RU_DIR}/${POT_FILE_STEM}.po"

    if [ -f "$RU_PO_PATH" ]; then
        echo "Po file exists, merging: ${POT_FILE_STEM}.po"
        msgmerge --backup=off --update "$RU_PO_PATH" "$POT_FILE_PATH"
    else
        echo "Po file missing, initializing: ${POT_FILE_STEM}.po"
        msginit --no-translator --locale=ru_RU --input "$POT_FILE_PATH" --output-file "$RU_PO_PATH"
    fi
done

rm -r "$BUILD_DIR"
