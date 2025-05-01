#!/bin/bash

DB_HOST=${POSTGRES_HOST:-db}
DB_PORT=${POSTGRES_PORT:-5432}

echo "⏳ Esperando a PostgreSQL en $DB_HOST:$DB_PORT..."

# Esperar hasta que PostgreSQL esté listo
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  echo "Postgres aún no disponible — esperando..."
  sleep 1
done

echo "✅ PostgreSQL está disponible. Ejecutando la aplicación..."

# Ejecutar migraciones y luego arrancar Gunicorn
python manage.py migrate && \
gunicorn config.wsgi:application --bind 0.0.0.0:8002
