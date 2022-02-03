# ping2

## What is this

It contacts ping1 to get its data, and returns it to you.

## Running locally

First, ensure ping1 is running at <http://localhost:5000/>. Then run the below commands.

    pipenv install
    PING1_URL="http://localhost:5000/" pipenv run python ping2.py

## Build docker image

    docker build ./ --tag henryfbp/ping2:latest


### Test local docker image

First, ensure ping1 is running at <http://localhost:80/>. Then run the below commands.

    docker run --detach --env PING1_SERVER="http://localhost:80/" --publish 81:5001 henryfbp/ping2:latest
    echo "Visit http://localhost:81/ping2"

