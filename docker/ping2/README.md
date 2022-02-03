# ping2

## What is this

It contacts ping1 to get its data, and returns it to you.

## Running locally

    pipenv install
    PING1_SERVER="http://localhost:5000/"; pipenv run python ping2.py

## Build docker image

    docker build ./ --tag henryfbp/ping2:latest


### Test local docker image

    docker run --detach --publish 81:5001 henryfbp/ping2:latest
    echo "Visit http://localhost:81/ping2"

