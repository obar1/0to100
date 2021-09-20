#!/usr/bin/env bash
set -u
set -o pipefail
set -e
set -x
# v0.1

###################
# setup
#################
h1(){
  echo "***[ $1 ]***"
}

help(){
  h1 "help"
  cat << EOF
  bash ${0} tag dir_repo
  ex
  bash ${0} 0.1 /tmp/some_dir/repo
EOF
}

get_code(){
  h1 "getting $1 in $2"
  ZEROto100=0to100
  TAG="${1}"
  DIR_TARGET="${2}"
  DIR_TARGET_LATEST="${2}/${ZEROto100}-latest"

  mkdir -p "${DIR_TARGET}"
  cd "${DIR_TARGET}"

  wget https://raw.githubusercontent.com/obar1/0to100/main/zero_to_one_hundred/tests/resources/repo/map.yaml
  sed -i '' -e "s|./repo|$DIR_TARGET|g" map.yaml

  cat map.yaml

  wget -qO- https://github.com/obar1/${ZEROto100}/archive/refs/tags/${TAG}.tar.gz | tar -xvf -
  mv "${ZEROto100}-${TAG}" "${DIR_TARGET_LATEST}"
}

echo_add_profile(){
  h1 "! add this to the ~/ .bashrc or .zshrc"
  CONFIG_FILE="${2}/map.yaml"
  ZEROto100py="${2}/${ZEROto100}-latest/zero_to_one_hundred/main.py"

cat << EOF
  export CONFIG_FILE="${CONFIG_FILE}"
  export ZEROto100py="${ZEROto100py}"

  function create_section() {
    python \$ZEROto100py create_section \$1
  }
  function refresh_map() {
    python \$ZEROto100py refresh_map
  }
  function refresh_links() {
    python \$ZEROto100py refresh_links
  }
  function refresh_puml() {
    python \$ZEROto100py refresh_puml
  }
EOF
}


help
get_code "$@"
echo_add_profile "$@"
set -x
ls -1 "${2}"
