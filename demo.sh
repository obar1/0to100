#!/bin/bash
# simple demo - it use param from cmd line to run the actual section

# set -x


# repo path
REPO_PATH="./0to100"

function setup {
    # set -x
    export MAP_YAML_PATH=map.yaml
    if [ ! -d ".venv" ]; then

        make setup
        chmod +x main.py
    fi
    . .venv/bin/activate
}
function setup_zo {
    cp ./tests/tests_zo/resources/map.yaml map.yaml
}

function setup_sb {
    cp ./tests/tests_sb/resources/map.yaml map.yaml
}

function zo {
    # 0to100
    setup_zo
    content=$(
        cat <<'EOF'
https://www.cloudskillsboost.google/123
https://www.udemy.com/course/python-for-beginners-hands-on/
https://www.youtube.com/watch?v=x7X9w_GIm1s
EOF
    )
    while IFS= read -r section || [[ -n "$section" ]]; do
        uv run ./main.py zo create_section "$section"
    done <<<"$content"

    echo "# a_custom_header 0" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "some txt" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "\`\`\`py" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "    this is code" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "    # with comments" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "\`\`\`" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"
    echo "## other sections" >> "$REPO_PATH/https§§§www.cloudskillsboost.google§123/readme.md"

    uv run ./main.py zo done_section "https://www.cloudskillsboost.google/123"

    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image.png
    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-1.png
    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-2.png


    # add some images ref
    echo -e "![alt text](image.png)\n">>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md
    echo -e "![some text](image-1.png)\n" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md
    echo -e "![](image-2.png)\n" >>"$REPO_PATH"/https§§§www.cloudskillsboost.google§123/readme.md

    touch "$REPO_PATH"/https§§§www.cloudskillsboost.google§123/image-3.png
    uv run ./main.py zo refresh_section_contents
    # image-3.png got deleted
    uv run ./main.py zo refresh_map

}

function sb {
    # 0to100 safari books
    setup_sb

    uv run ./main.py sb snatch_book https://learning.oreilly.com/course/clean-code-fundamentals/9780134661742
    echo 'add any metadata you like'
    echo '{"title": "Clean Code Fundamentals","page_curr": "99", "page_tot": "100"}' >"$REPO_PATH"/9780134661742/9780134661742.json
    uv run ./main.py sb refresh_toc

    uv run ./main.py sb snatch_book https://learning.oreilly.com/library/view/rewire-your-brain/9781119895947
    echo 'pretend book was read fully and get % calc for free :P'
    echo '{"page_curr": "100", "page_tot": "100", "url":"https://www.oreilly.com/library/view/rewire-your-brain/9781119895947"}' >"$REPO_PATH"/9781119895947/9781119895947.json
    uv run ./main.py sb refresh_toc

}

#!/bin/bash

if [ $# -eq 0 ]; then
    echo "use zo or sb"

else
    setup
    $1
fi
