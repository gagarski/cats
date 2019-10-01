#!/bin/bash

pushd "$(dirname "${BASH_SOURCE[0]}")"

if [[ ! -e .env ]]; then
    virtualenv -ppython3.7 .env
fi

if [[ ! -e settings.py ]]; then
    cp settings.py.template settings.py
fi

git submodule init
git submodule update

popd