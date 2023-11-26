#!/usr/bin/env bash

set -e

kata_name=$1
kata_dir="katas/$kata_name"
solution_file="$kata_dir/solution.py"
test_file="$kata_dir/test.py"

function main() {
  validate_args
  mkdir "$kata_dir"
  make_solution_file
  make_test_file
  open_test_file

  echo "Kata directory created at $kata_dir"
}

function validate_args() {
  if [ -z "$kata_name" ]; then
    echo "No first argument was passed."
    exit
  fi
}

function make_solution_file() {
  touch "$solution_file"

  file=$(cat templates/solution.txt)
  replaced_file=${file//\$funcName\$/$kata_name}

  echo "$replaced_file" >"$solution_file"
}

function make_test_file() {
  touch "$test_file"

  file=$(cat templates/spec.txt)
  replaced_file=${file//\$funcName\$/$kata_name}

  echo "$replaced_file" >"$test_file"
}

function open_test_file() {
  pycharm "$test_file"
}

main
