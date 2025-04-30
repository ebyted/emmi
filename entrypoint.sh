#!/bin/bash
# Cargar variables desde .env
export $(grep -v '^#' .env | xargs)

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor gunicorn
gunicorn backend.wsgi:application --bind 0.0.0.0:8000