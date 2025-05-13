#!/bin/bash
PROJECT_PATH=$(dirname $(realpath $0))

# Python auto detect
PYTHON_CMD=$(which python3 || which python)

$PYTHON_CMD ${PROJECT_PATH}/manage.py dumpdata --indent 4 > sample_data.json
