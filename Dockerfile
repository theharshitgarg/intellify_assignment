FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /app


COPY requirements.txt /app
COPY ./ /app


RUN pip install -r /app/requirements.txt

WORKDIR /app/intellify_backend
