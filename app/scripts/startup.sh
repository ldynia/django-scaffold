#!/bin/ash

pip install --upgrade pip --no-cache-dir
pip install -r /app/requirements.txt --no-cache-dir

python /app/manage.py migrate
#python /app/manage.py createsuperuser
python /app/manage.py runserver 0.0.0.0:8000

sleep 3600