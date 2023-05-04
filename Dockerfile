FROM python:3.9

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate

ENV DJANGO_DB_FILE=/data/db.sqlite3
