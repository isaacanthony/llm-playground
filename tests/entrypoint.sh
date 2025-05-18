#!/bin/sh

echo
echo "running black..."
black --diff /src

echo
echo "runing pylint..."
pylint \
    --disable=c-extension-no-member \
    --disable=import-error \
    --disable=missing-class-docstring \
    --disable=missing-function-docstring \
    --disable=missing-module-docstring \
    --disable=no-name-in-module \
    --disable=too-few-public-methods \
    --disable=unused-argument \
    --disable=unused-import \
    /src
