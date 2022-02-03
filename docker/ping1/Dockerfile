FROM python:3.9.10-slim-buster

RUN pip install pipenv

WORKDIR /app
COPY . .

RUN pipenv install
EXPOSE 5000/tcp
CMD ["pipenv", "run", "python", "ping1.py"]