FROM python:3.11

WORKDIR /app

COPY . /app
COPY .env /app/.env

RUN pip install --upgrade pip
RUN pip install -r requiriments.txt

ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]