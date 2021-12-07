FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./

RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .
