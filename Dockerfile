FROM python:3.7-alpine
MAINTAINER Amir Mallaei

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

Run mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user
