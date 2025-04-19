#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

REPO_PATH="./0to100"

function setup {
    # set -x
    if [ ! -d "venv" ]; then
        export MAP_YAML_PATH=map.yaml
        make setup
        chmod +x main.py
    fi
}
function setup_zo {
    cp ./zero_to_one_hundred/tests/tests_zo/resources/map.yaml map.yaml
}

function setup_sb {
    cp ./zero_to_one_hundred/tests/tests_sb/resources/map.yaml map.yaml
}

function setup_yt {
    cp ./zero_to_one_hundred/tests/tests_yt/resources/map.yaml map.yaml
}

function zo {
    # 0to100
    setup_zo

    ./main.py zo help
    content=$(
        cat <<'EOF'
https://www.cloudskillsboost.google/123
https://www.cloudskillsboost.google/paths=16
https://www.cloudskillsboost.google/games/4424/labs/28651
https://www.cloudskillsboost.google/course_templates/3
https://www.udemy.com/course/python-for-beginners-hands-on/
https://www.youtube.com/watch?v=W_AdDqdwW90
EOF
    )
    while IFS= read -r section || [[ -n "$section" ]]; do
        ./main.py zo create_section "$section"
    done <<<"$content"

    echo "# a_custom_header 0" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md

    ./main.py zo done_section "https://www.cloudskillsboost.google/123"

    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image.png
    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-1.png
    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-2.png
    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-3.png

    echo "some text" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md
    echo "![alt text](image.png)">>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md
    echo "![some text](image-1.png)" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md
    echo "![](image-2.png)" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md

    ./main.py zo refresh_section_contents
    # image-3.png got deleted 

}

function sb {
    # 0to100 safari books
    setup_sb

    ./main.py sb help

    ./main.py sb snatch_book https://learning.oreilly.com/course/clean-code-fundamentals/9780134661742
    echo 'add any metadata you like'
    echo '{"title": "Clean Code Fundamentals","page_curr": "99", "page_tot": "100"}' >"$REPO_PATH"/9780134661742/9780134661742.json
    ./main.py sb refresh_toc

    ./main.py sb snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947
    echo 'pretend book was read fully and get % calc for free :P'
    echo '{"page_curr": "100", "page_tot": "100", "url":"https://www.oreilly.com/library/view/rewire-your-brain/9781119895947"}' >"$REPO_PATH"/9781119895947/9781119895947.json
    ./main.py sb refresh_toc

}

function yt {
    # 0to100 safari books
    setup_sb

    ./main.py yt help

    content=$(
        cat <<'EOF'
https://www.youtube.com/watch?v=aTCeAtzzekw
https://www.youtube.com/watch?v=-Y44YzIODw0
EOF
    )
    while IFS= read -r section || [[ -n "$section" ]]; do
        ./main.py yt snatch_yt  "$section"
    done <<<"$content"
}


#!/bin/bash

if [ $# -eq 0 ]; then
    echo "No arguments were passed: use sb zo or yt"
else
    setup
    $1
fi
