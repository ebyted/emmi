FROM python:3.11

WORKDIR /app

RUN apt-get update && \
    apt-get install -y gcc libpq-dev netcat postgresql-client && \
    apt-get clean

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN chmod +x /app/wait-for-db.sh