FROM python:3.8-slim


WORKDIR /usr/src/bookingsite



ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY ./requirements.txt .

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

RUN pip install -r requirements.txt

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/bookingsite/entrypoint.sh
RUN chmod +x /usr/src/bookingsite/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
COPY entrypoint.sh /usr/src/bookingsite/

RUN ["chmod", "+x", "./entrypoint.sh"]
