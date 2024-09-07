#!/bin/bash
# simple demo - it use param from cmd line to run the actual section
# v0.1

function setup {
    set -x
    export MAP_YAML_PATH=map.yaml
    
    rm -rf safaribooks/
    
    pip install .
    
    chmod +x main*.py
}
function setup0to100 {
    rm -rf 0to100/
    
    cp ./zero_to_one_hundred/tests/test_ztoh/resources/gcp_map.yaml map.yaml
}

function setup0to100_sb {
    rm -rf 978*/
    
    cp ./zero_to_one_hundred/tests/tests_sb/resources/map.yaml map.yaml
    
    # safari books from lorenzodifuccia
    git clone https://github.com/lorenzodifuccia/safaribooks.git
    pip install --quiet -r safaribooks/requirements.txt
}

function 0to100 {
    # 0to100
    setup0to100
    
    ./main.py help
#    - name: Course
#    - name: Game
#    - name: Lab
#    - name: Quest
#    - name: Template
content=$(cat << 'EOF'
https://www.cloudskillsboost.google/games/4424/labs/28651
https://www.cloudskillsboost.google/course_templates/3
https://www.cloudskillsboost.google/games/4422
https://storage.googleapis.com/cloud-training/cls-html5-courses/T-BQRS-I/M1/index.html

EOF
)
while IFS= read -r line || [[ -n "$line" ]]; do
    echo "Processing: $line"

  ./main.py create_section "$line"
done <<< "$content"


    ls -1R 0to100
}

function 0to100_sb {
    # 0to100 safari books
    setup0to100_sb
    
    ./main_sb.py help
    
    ./main_sb.py snatch_book https://learning.oreilly.com/course/clean-code-fundamentals/9780134661742
    echo 'add any metadata you like'
    echo '{"title": "Clean Code Fundamentals"}'> 9780134661742/9780134661742.json
    ./main_sb.py refresh_toc
    
    ./main_sb.py snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947
    echo 'pretend book was read fully and get % calc for free :P'
    echo '{"page_curr": "100", "page_tot": "100", "url":"https://www.oreilly.com/library/view/rewire-your-brain/9781119895947"}' > 9781119895947/9781119895947.json
    ./main_sb.py refresh_toc
    
    ls -1R 978*
}

setup
$1
