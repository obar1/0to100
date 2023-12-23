#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

function setup {
    # set -x
    rm -rf safaribooks/

    pip install .
    rm -rf build/

    chmod +x main*.py
}
function setup0to100 {
    cp ./zero_to_one_hundred/tests/resources/map.yaml .
    export MAP_YAML_PATH=$(pwd)/map.yaml
}

function setup0to100_sb {
    rm -rf 0to100*/

    cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
    export MAP_YAML_PATH=$(pwd)/map.yaml

    # safari books from lorenzodifuccia
    git clone https://github.com/lorenzodifuccia/safaribooks.git
    pip install --quiet -r safaribooks/requirements.txt
}

function 0to100 {
    # 0to100
    setup0to100

    ./main.py help

    url=https://cloud.google.com/docs/
    ./main.py create_section "$url"

    url=https://docs.getdbt.com/docs/introduction
    ./main.py create_section "$url"

    url=https://cloud.google.com/docs/
    ./main.py done_section "$url"

    ls -1R 0to100
}

function 0to100_sb {
    # 0to100 safari books
    setup0to100_sb

    ./main_sb.py help

    url=https://learning.oreilly.com/library/view/the-pragmatic-programmer/9780135956977/
    ./main_sb.py create_meta_book "$url"

    url=https://learning.oreilly.com/library/view/head-first-design/9781492077992/
    ./main_sb.py create_meta_book "$url"

    ./main_sb.py refresh_toc

    ls -1R 978*
}

setup
$1
