# pingn

## What is this

Example of server that either asks another server for data, or serves data on its own.

## Running locally

To make 3 servers:

    pipenv install
    IS_ROOT_PING=1 APP_NAME=ping1 PORT=5001 pipenv run python pingn.py

## Build docker image

    docker build ./ --tag henryfbp/pingn:latest


### Test local docker image

TODO change this

First, ensure ping1 is running at <http://localhost:80/>. Then run the below commands.

    docker run --detach --env CHILD_URL="http://localhost:80" --publish 81:5001 henryfbp/ping2:latest
    echo "Visit http://localhost:81/ping2"

