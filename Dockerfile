FROM python:3.11

WORKDIR /code

# Instala netcat y cliente PostgreSQL (para pg_isready)
RUN apt-get update && \
    apt-get install -y netcat-openbsd postgresql-client && \
    apt-get clean

COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
COPY wait-for-db.sh /code/wait-for-db.sh
RUN chmod +x /code/wait-for-db.sh

CMD ["./wait-for-db.sh", "db", "bash", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:8002"]
