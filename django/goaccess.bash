#!/bin/bash

PROJECT_PATH=$(dirname $(realpath $0))

LOG_DIR_PATH=${PROJECT_PATH}/logs/nginx
ACCESS_LOG_PATH=${LOG_DIR_PATH}/access.log

STATIC_DIR_PATH=${PROJECT_PATH}/static
OUTPUT_PATH=${STATIC_DIR_PATH}/goaccess.html

echo -e "\nStart GoAccess"

while true
do
  goaccess ${ACCESS_LOG_PATH} \
    -o ${OUTPUT_PATH} \
    --log-format='%d:%t %^ "%r" %s %b "%R" "%u" %h %^ %T %^ %H %m %v %^ %b %^ %^ "%^" "%^" "%^"' \
    --date-format='%d/%b/%Y' \
    --time-format='%T' \
    --persist \
    --restore
    sleep 10
done
