#!/bin/bash

service nginx start
service supervisor start
./django/start.uwsgi.bash
