#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

function setup {
    # set -x
    export MAP_YAML_PATH=map.yaml

    pip install .

    chmod +x main.py
}
function setup_zo {
    cp ./zero_to_one_hundred/tests/tests_zo/resources/gcp_map.yaml map.yaml
}

function setup_sb {
    cp ./zero_to_one_hundred/tests/tests_sb/resources/map.yaml map.yaml

    # safari books from lorenzodifuccia
    git clone https://github.com/lorenzodifuccia/safaribooks.git
    pip install --quiet -r safaribooks/requirements.txt
}

function zo {
    # 0to100
    setup_zo

    ./main.py zo help
    content=$(
        cat <<'EOF'
https://www.cloudskillsboost.google/0
https://www.cloudskillsboost.google/paths/16
https://www.cloudskillsboost.google/games/4424/labs/28651
https://www.cloudskillsboost.google/course_templates/3
https://www.cloudskillsboost.google/games/4422
https://storage.googleapis.com/cloud-training/cls-html5-courses/T-BQRS-I/M1/index.html
EOF
    )
    while IFS= read -r section || [[ -n "$section" ]]; do
        ./main.py zo create_section "$section"
    done <<<"$content"

    echo "# a_custom_header 0" >>0to100/https§§§www.cloudskillsboost.google§0/readme.md

    ./main.py zo done_section "https://www.cloudskillsboost.google/0"

    touch 0to100/https§§§www.cloudskillsboost.google§0/image.png
    touch 0to100/https§§§www.cloudskillsboost.google§0/image-1.png
    touch 0to100/https§§§www.cloudskillsboost.google§0/image-2.png
    touch 0to100/https§§§www.cloudskillsboost.google§0/image-3.png

    echo "some text" >>0to100/https§§§www.cloudskillsboost.google§0/readme.md
    echo "![alt text](image.png)">>0to100/https§§§www.cloudskillsboost.google§0/readme.md
    echo "![some text](image-1.png)" >>0to100/https§§§www.cloudskillsboost.google§0/readme.md
    echo "![](image-2.png)" >>0to100/https§§§www.cloudskillsboost.google§0/readme.md

    ./main.py zo refresh_section_contents
    # image-3.png got deleted 

    ls -1R 0to100
    cp toc.md toc_zo.md
}

function sb {
    # 0to100 safari books
    setup_sb

    ./main.py sb help

    ./main.py sb snatch_book https://learning.oreilly.com/course/clean-code-fundamentals/9780134661742
    echo 'add any metadata you like'
    echo '{"title": "Clean Code Fundamentals"}' >9780134661742/9780134661742.json
    ./main.py sb refresh_toc

    ./main.py sb snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947
    echo 'pretend book was read fully and get % calc for free :P'
    echo '{"page_curr": "100", "page_tot": "100", "url":"https://www.oreilly.com/library/view/rewire-your-brain/9781119895947"}' >9781119895947/9781119895947.json
    ./main.py sb refresh_toc

    ls -1R 978*
    cp toc.md toc_sb.md

}

#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No arguments were passed: use sb or zo"
else
    setup
    $1
fi
