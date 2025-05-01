# Base image
FROM python:3.11

# Crear entorno virtual
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Instalar dependencias
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copiar el resto del código
COPY . /app
WORKDIR /app

# Comando para ejecutar la app
CMD ["python", "app.py"]
