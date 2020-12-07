#!/bin/ash

echo "Install requirements.txt"
pip install --upgrade pip --no-cache-dir
pip install -r /app/requirements.txt --no-cache-dir

echo "Run migrations"
python /app/manage.py migrate
# python /app/manage.py createsuperuser

# Check if args $@ is empty 
if [ -z "$@" ]
then
    echo "Run server"
    python /app/manage.py runserver 0.0.0.0:8000
else
    echo "Execute \$@ command"
    exec $@
fi

