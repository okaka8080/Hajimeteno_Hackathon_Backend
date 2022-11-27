FROM python:3.8

RUN mkdir -p /opt
COPY . /opt
WORKDIR /opt

RUN apt update
RUN apt-get install -y libgl1-mesa-dev
RUN apt install -y libpq-dev build-essential
RUN pip install pipenv
RUN pipenv install --skip-lock