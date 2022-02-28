FROM python:3.8

RUN pip install pipenv

RUN apt update
RUN apt install -y iputils-ping curl
RUN apt install -y libpq-dev python3-dev

WORKDIR /app/

COPY Pipfile ./
COPY Pipfile.lock ./
RUN pipenv install

COPY ./pingn/ /app/
EXPOSE 5000

CMD ["pipenv", "run", "python", "pingn/__main__.py"]
