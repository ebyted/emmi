# Imagen base de Python
FROM python:3.11-slim

# Crear y usar el directorio de trabajo
WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install --root-user-action=ignore -r requirements.txt

EXPOSE 8002

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8002"]