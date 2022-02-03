# Running locally

    pipenv install
    pipenv run python ping1.py

# Build docker image

    docker build ./ --tag henryfbp/ping1:latest

## Test local docker image

    docker run -d -p 80:5000 henryfbp/ping1:latest
    echo "Visit http://localhost:80/ping1"

## delete container

    docker images
    docker rmi 1234abcd

## stop the container

    docker ps
    docker stop 1234abcd

## get shell into running container

    docker ps
    docker exec -it 1234abcd /bin/bash

# Notes

https://sourcery.ai/blog/python-docker/