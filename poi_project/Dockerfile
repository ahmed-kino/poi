FROM python:3.11.5-alpine

ENV PYTHONUNBUFFERED 1

RUN apk update && apk add make

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt


RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]