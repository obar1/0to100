#!/bin/bash
# set -x
# python -m venv .venv || true TODO:
. ./venv/bin/activate
# pip install -r requirements.txt

chmod +x main*.py


export MAP_YAML_PATH=$(pwd)/map.yaml

# 0to100
cp ./zero_to_one_hundred/tests/resources/map.yaml .
./main.py

url=https://cloud.google.com/docs/
./main.py create_section "$url"
url=https://docs.getdbt.com/docs/introduction
./main.py create_section "$url"
url=https://cloud.google.com/docs/
./main.py done_section "$url"

# 0to100 safari books
cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .

 