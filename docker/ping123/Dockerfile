FROM python:3.9.10-slim-buster

RUN pip install pipenv

RUN apt update
RUN apt install -y iputils-ping curl

WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

COPY ./pingn/ .
EXPOSE 5000
CMD ["pipenv", "run", "python", "-m", "pingn"]
