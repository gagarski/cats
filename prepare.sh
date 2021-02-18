#!/bin/bash

pushd "$(dirname "${BASH_SOURCE[0]}")"

if [[ ! -e .env ]]; then
    virtualenv -ppython3.9 .env
fi

source .env/bin/activate
pip install -r requirements.txt
deactivate

if [[ ! -e settings.py ]]; then
    cp settings.py.template settings.py
fi

git submodule init
git submodule update

popd
