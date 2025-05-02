#!/bin/sh

# Espera a que Postgres esté listo con pg_isready
echo "Esperando a la base de datos en $1:5432..."

until pg_isready -h "$1" -p 5432; do
  echo "⏳ Esperando a DB..."
  sleep 1
done

echo "✅ DB lista. Ejecutando comandos..."

shift
exec "$@"