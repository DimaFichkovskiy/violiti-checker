FROM python:3.10.1-alpine

ENV DEBUG true

COPY . /bot

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev
RUN apk add build-base


RUN pip install -r bot/requirements.txt

CMD python3 bot/app.py