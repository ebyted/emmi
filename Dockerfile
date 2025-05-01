# Imagen base de Python
FROM python:3.11-slim

# Crear y usar el directorio de trabajo
WORKDIR /app

# Copiar el contenido del proyecto al contenedor
COPY . /app

# Instalar netcat para comprobaciones opcionales de red
RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean

# Instalar dependencias Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Exponer el puerto que usará gunicorn (coincide con docker-compose:8002)
EXPOSE 8002

# Comando para ejecutar gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8002", "backend.wsgi:application"]