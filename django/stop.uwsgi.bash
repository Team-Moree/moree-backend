#!/bin/bash

PROJECT_PATH=$(dirname $(realpath $0))

UWSGI_CONFIG_PATH=${PROJECT_PATH}/uwsgi.ini

RUN_DIR_PATH=${PROJECT_PATH}/run
SOCKET_PATH=${RUN_DIR_PATH}/uwsgi.sock
PID_PATH=${RUN_DIR_PATH}/uwsgi.pid

LOG_DIR_PATH=${PROJECT_PATH}/logs
LOG_PATH=${LOG_DIR_PATH}/uwsgi.log

if [ -f "${PID_PATH}" ]; then
    kill -9 "$(cat ${PID_PATH})"
    echo "uWSGI Process(PID : $(cat ${PID_PATH})) was killed"
    rm "${PID_PATH}"
    echo "Delete ${PID_PATH}"
    rm "${SOCKET_PATH}"
    echo "Delete ${SOCKET_PATH}"
    rm "${UWSGI_CONFIG_PATH}"
    echo "Delete ${UWSGI_CONFIG_PATH}"
fi
