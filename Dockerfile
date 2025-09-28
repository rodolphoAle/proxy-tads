FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requiriments.txt

EXPOSE 5000

CMD ["python", "app.py"]