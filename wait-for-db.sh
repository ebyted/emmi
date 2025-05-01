#!/bin/bash

echo "⏳ Esperando a que PostgreSQL esté disponible..."

until nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
  echo "Postgres aún no responde en $POSTGRES_HOST:$POSTGRES_PORT - durmiendo"
  sleep 1
done

echo "✅ PostgreSQL está disponible — continuando..."
exec "$@"