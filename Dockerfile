FROM python:3.10-alpine

WORKDIR /usr/src/

COPY src/requirements.txt .
RUN pip3 install -r requirements.txt
COPY src/ ./

