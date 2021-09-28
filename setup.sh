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
  mv "${ZEROto100}-${TAG}" "${DIR_TARGET_LATEST}" || true

  # DEBUG
}

create_runme(){
  h1 "! use this to run"

cat <<EOF >runme.sh
  export CONFIG_FILE="${2}/map.yaml"
  export ZEROto100py="${2}/${ZEROto100}-latest/zero_to_one_hundred/main.py"
  # main at run time
  python \$ZEROto100py "\$@"
EOF

ls *.sh
}


help
get_code "$@"
create_runme "$@"
