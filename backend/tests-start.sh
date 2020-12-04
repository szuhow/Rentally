#!/usr/bin/env bash

# Exit immediately if command exits with a non-zero status.
set -e

python3 ./app/tests_pre_start.py

bash ./scripts/test.sh "$@"
