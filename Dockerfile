FROM python:3.11

WORKDIR /code

# Instalación de dependencias del sistema
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat-openbsd postgresql-client && \
    apt-get clean
RUN cat .env


# Copia e instalación de dependencias de Python
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia del proyecto y del script de espera
COPY . /code/
COPY wait-for-db.sh /code/wait-for-db.sh
RUN chmod +x /code/wait-for-db.sh

# Comando por defecto para iniciar la app
CMD ["sh", "-c", "./wait-for-db.sh db bash -c 'python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8002'"]
