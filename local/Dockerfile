FROM python:3

COPY ./ ./

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ENV STATIC_PATH ./static