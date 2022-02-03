# ping1

## What is this?

simple example of a python api. It just returns some sample json. It does not depend on other services.

## Running locally

    pipenv install
    pipenv run python ping1.py

## Build docker image

    docker build ./ --tag henryfbp/ping1:latest

### upload to docker hub (only if you're henryfbp)

    docker login
        (le creds)
    docker push henryfbp/ping1

### Test local docker image

    docker run --detach --publish 80:5000 henryfbp/ping1:latest
    echo "Visit http://localhost:80/ping1"

### delete image

    docker images
    docker rmi 1234abcd

### stop the container

    docker ps
    docker stop 1234abcd

### get shell into running container

    docker ps
    docker exec --tty --interactive 1234abcd /bin/bash

### get logs of running container (stdout/stderr)

    docker ps
    docker logs 1234abcd --tail

## Notes

https://sourcery.ai/blog/python-docker/