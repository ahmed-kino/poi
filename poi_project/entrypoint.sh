#!/bin/sh

env | grep DJANGO
env | grep POSTGRES
# Start server
echo "Starting server"
python ./manage.py runserver 0.0.0.0:8000