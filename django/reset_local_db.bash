#!/bin/bash
PROJECT_PATH=$(dirname $(realpath $0))

USER=administrator
GROUP=administrator

DJANGO_SUPERUSER_USERNAME=root
DJANGO_SUPERUSER_PASSWORD=root
DJANGO_SUPERUSER_EMAIL=test@test.com

APP_LIST=(common governance sample)

APP_PATH_LIST=()
for app in ${APP_LIST[@]}
do
    APP_PATH_LIST+=(${PROJECT_PATH}/${app})
done

TARGET_LIST=(${PROJECT_PATH}/db.sqlite3)

for app_path in ${APP_PATH_LIST[@]}
do
    TARGET_LIST+=(${app_path}/migrations/$(ls ${app_path}/migrations | grep '[0-9]\{4\}.*' || true))
done


for target_path in ${TARGET_LIST[@]}
do
    echo "Delete ${target_path}"
    rm -rf ${target_path}
done

# Python auto detect
PYTHON_CMD=$(which python3 || which python)

# migration
for app in ${APP_LIST[@]}
do
    $PYTHON_CMD ${PROJECT_PATH}/manage.py makemigrations ${app}
done
$PYTHON_CMD ${PROJECT_PATH}/manage.py migrate

chown -R ${GROUP}:${USER} ${PROJECT_PATH}

export DJANGO_SUPERUSER_USERNAME=${DJANGO_SUPERUSER_USERNAME}
export DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD}
export DJANGO_SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL}

$PYTHON_CMD ${PROJECT_PATH}/manage.py createsuperuser --noinput

$PYTHON_CMD ${PROJECT_PATH}/manage.py loaddata sample_data.json

# Insert test data
#$PYTHON_CMD ${PROJECT_PATH}/manage.py insert_test_data
