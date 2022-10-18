FROM python:3.8

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade pip

RUN pip install -r requirements.txt

COPY src /app