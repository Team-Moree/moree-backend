#!/bin/bash
PROJECT_PATH=$(dirname $(realpath $0))

# Python auto detect
PYTHON_CMD=$(which python3 || which python)

$PYTHON_CMD ${PROJECT_PATH}/manage.py loaddata sample_data.json
