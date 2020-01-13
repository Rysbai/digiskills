FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/digiskills

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/digiskills/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/digikills/entrypoint.sh

# copy project
COPY . /usr/src/digiskills/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/digiskills/entrypoint.sh"]