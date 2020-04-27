FROM python:3.6

COPY . /code/
WORKDIR /code/


RUN pip3 install django gunicorn

EXPOSE 8000

CMD gunicorn UsrDocker.wsgi:application --bind 0.0.0.0:8000
