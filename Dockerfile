FROM python:3.11

WORKDIR /app

# Instalación de dependencias del sistema
RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat postgresql-client && \
    apt-get clean

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el script a una ruta que no se monte
COPY wait-for-db.sh /scripts/wait-for-db.sh
RUN chmod +x /scripts/wait-for-db.sh

# Copiar el resto del código de la app
COPY . /app/