FROM python:3.12

# Gunicorn and Django

RUN pip install gunicorn json-logging django

COPY docker/logging.conf /logging.conf
COPY docker/gunicorn.conf /gunicorn.conf

EXPOSE 3001
WORKDIR /app/
VOLUME /app/media/
VOLUME /app/static/

ENTRYPOINT /usr/local/bin/gunicorn --config /gunicorn.conf --log-config /logging.conf -b :3001 portfolio.wsgi

# Portfolio

RUN apt-get update \
  && apt-get install -y gettext

ADD requirements.txt /app/
RUN pip install -r /app/requirements.txt

ADD . /app/

