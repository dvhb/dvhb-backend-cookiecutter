#!/bin/sh
set -e

until psql -h "db" -U "postgres" -c '\l'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

COMMAND="python manage.py"

${COMMAND} makemigrations --no-input && ${COMMAND} migrate --no-input && exec ${COMMAND} runserver --noreload 0.0.0.0:8000
