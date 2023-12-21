#!/bin/bash
function setup {
    # set -x
    # python -m venv .venv || true TODO:
    . ./venv/bin/activate
    # pip install -r requirements.txt

    chmod +x main*.py

    export MAP_YAML_PATH=$(pwd)/map.yaml
}

function 0to100 {
    cls
    # 0to100

    cp ./zero_to_one_hundred/tests/resources/map.yaml .
    ./main.py

    url=https://cloud.google.com/docs/
    ./main.py create_section "$url"
    url=https://docs.getdbt.com/docs/introduction
    ./main.py create_section "$url"
    url=https://cloud.google.com/docs/
    ./main.py done_section "$url"

    ls -1R 0to100
}

function 0to100_sb {
    cls
    # 0to100 safari books
    cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
    ./main_sb.py

    url=https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/
    ./main_sb.py create_meta_book "$url"

    ls -1R 9780135956977
}

setup
# 0to100
0to100_sb
