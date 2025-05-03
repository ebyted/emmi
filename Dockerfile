FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "emmi.wsgi:application", "--bind", "0.0.0.0:8002"]
