#!/bin/bash

python /app/manage.py migrate
#python /app/manage.py createsuperuser
python /app/manage.py runserver 0.0.0.0:80
