FROM python:3.8

#set environment variabels
ENV PYTHONDONTWRITEBYTE 1
ENV PYTHONUNBUFFERED 1

#SET WORK DIR
WORKDIR /code

#install dependincies
COPY pipfile pipfile.lock /code/
RUN pip instal pipenv && pipenv install --system

#Copy project
COPY . /code/
