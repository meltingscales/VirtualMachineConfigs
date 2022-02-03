FROM python:3.9.10-slim-buster

RUN pip install pipenv


WORKDIR /app

COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

COPY . .
EXPOSE 5002
CMD ["pipenv", "run", "python", "ping3.py"]