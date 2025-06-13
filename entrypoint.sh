#!/bin/bash

# Wait for the database to be ready
echo "Waiting for PostgreSQL to start..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done
echo "PostgreSQL started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Start the server
echo "Starting server..."
if [ "$DJANGO_ENV" = "production" ]; then
    daphne -b 0.0.0.0 -p 8000 streaming_platform.asgi:application
else
    python manage.py runserver 0.0.0.0:8000
fi