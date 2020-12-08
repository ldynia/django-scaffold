#!/bin/ash

echo "Install requirements.txt"
pip install -r /app/requirements.txt --no-cache-dir

echo "Run migrations"
python /app/manage.py migrate

# is $@ empty 
if [ -z "$@" ]
then
    echo "Run Server"
    python /app/manage.py runserver 0.0.0.0:$PORT
else
    echo "Executeing \$@ command: $@"
    exec $@
fi