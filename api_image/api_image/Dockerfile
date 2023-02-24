# pull official base image

FROM python:3.9.6-alpine

# set work directory    # Disabled
# WORKDIR /usr/src/app


# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip3 install --upgrade pip
COPY ./requirements.txt .
#COPY  requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

# copy project
COPY . .

## CMD ["python","manage.py","runserver"]

EXPOSE 8000