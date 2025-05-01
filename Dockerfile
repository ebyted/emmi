FROM python:3.11

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat-openbsd postgresql-client && \
    apt-get clean

# Copiar los requirements
COPY requirements.txt ./

# Instalar dependencias Python
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . .

# Copiar script para esperar la DB
COPY wait-for-db.sh ./wait-for-db.sh
RUN chmod +x ./wait-for-db.sh

# Exponer el puerto en el que corre Gunicorn
EXPOSE 8002

# Comando final: esperar la DB y lanzar la app
CMD ["sh", "-c", "./wait-for-db.sh db bash -c 'python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8002'"]

