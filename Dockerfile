# Imagen base de Python
FROM python:3.11-slim

# Crear y usar el directorio de trabajo
WORKDIR /app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8002

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8002"]