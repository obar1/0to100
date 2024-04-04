#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

function setup {
    set -x
    export MAP_YAML_PATH=map.yaml
    
    rm -rf safaribooks/
    
    pip install .
    
    chmod +x main*.py
}
function setup0to100 {
    rm -rf 0to100/
    
    cp ./zero_to_one_hundred/tests/resources/gcp_map.yaml map.yaml
}

function setup0to100_sb {
    rm -rf 978*/
    
    cp ./zero_to_one_hundred/tests_sb/resources/map.yaml .
    
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
    
    url=https://learning.oreilly.com/course/clean-code-fundamentals/9780134661742/
    ./main_sb.py snatch_book "$url"
    echo 'add any metadata you like'
    echo '{"title": "Clean Code Fundamentals"}'> 9780134661742/9780134661742.json
    ./main_sb.py refresh_metadata "$url"
    
    url=https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947/
    ./main_sb.py snatch_book "$url"
    
    url=https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947/
    echo 'pretend book was read fully :P'
    echo '{"page_curr": "1", "page_tot": "1"}' > 9781119895947/9781119895947.json
    ./main_sb.py refresh_metadata "$url"
    
    ./main_sb.py refresh_toc
    
    ls -1R 978*
}

setup
$1
