#!/bin/bash

PROJECT_PATH=$(dirname $(realpath $0))

UWSGI_CONFIG_PATH=${PROJECT_PATH}/uwsgi.ini

RUN_DIR_PATH=${PROJECT_PATH}/run
SOCKET_PATH=${RUN_DIR_PATH}/uwsgi.sock
PID_PATH=${RUN_DIR_PATH}/uwsgi.pid

LOG_DIR_PATH=${PROJECT_PATH}/logs
LOG_PATH=${LOG_DIR_PATH}/uwsgi.log

USER_ID=root
GROUP_ID=root
PROCESSES=2
THREADS=4
LISTEN_QUEUE_SIZE=100

mkdir -p ${RUN_DIR_PATH}
mkdir -p ${LOG_DIR_PATH}

if [ -f "${PID_PATH}" ]; then
    kill -9 "$(cat ${PID_PATH})"
    echo "uWSGI Process(PID : $(cat ${PID_PATH})) was killed"
    rm "${PID_PATH}"
    echo "Delete ${PID_PATH}"
    rm "${SOCKET_PATH}"
    echo "Delete ${SOCKET_PATH}"
fi

echo -e "\nStart Django with uWSGI"
echo "[uwsgi]
chdir          = ${PROJECT_PATH}
module         = config.wsgi
processes      = ${PROCESSES}
treads         = ${THREADS}
listen         = ${LISTEN_QUEUE_SIZE}
master         = True
socket         = ${SOCKET_PATH}
pidfile        = ${PID_PATH}
daemonize      = ${LOG_PATH}
uid            = ${USER_ID}
gid            = ${GROUP_ID}
die-on-term    = true
enable-threads = true
vacuum         = true" > ${PROJECT_PATH}/uwsgi.ini
uwsgi --ini ${UWSGI_CONFIG_PATH}

echo -e "\n${UWSGI_CONFIG_PATH}"
cat ${UWSGI_CONFIG_PATH}
tail -f ${LOG_PATH}
