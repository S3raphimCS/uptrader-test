#!/bin/sh

python "manage.py" migrate --noinput

python "manage.py" collectstatic --noinput

python "manage.py" loaddata server/fixtures/example_data.json

gunicorn -c "$PROJECT_ROOT/gunicorn.conf.py" server.wsgi:application
