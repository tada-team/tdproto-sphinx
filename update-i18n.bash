#!/bin/bash
set -euo pipefail
shopt -s extdebug
IFS=$'\n\t'

BUILD_DIR="./build_gettext"
LOCALE_DIR="./docs/locale"

sphinx-build -b gettext "./docs" "$BUILD_DIR"

sphinx-intl update --locale-dir "$LOCALE_DIR" --pot-dir "$BUILD_DIR" --language=ru

rm -r "$BUILD_DIR"
