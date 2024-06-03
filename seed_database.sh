#!/bin/bash

rm db.sqlite3
rm -rf ./cultsapi/migrations
python3 manage.py migrate
python3 manage.py makemigrations cultsapi
python3 manage.py migrate cultsapi
python3 manage.py loaddata user
python3 manage.py loaddata token

