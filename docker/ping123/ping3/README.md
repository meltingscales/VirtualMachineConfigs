# ping3

## What is this

It contacts ping2 to get its data, and returns it to you.

## Running locally

First, ensure ping2 is running at <http://localhost:5001/>. Then run the below commands.

    pipenv install
    PING2_URL="http://localhost:5001/" pipenv run python ping3.py

## Build docker image

    docker build ./ --tag henryfbp/ping3:latest


### Test local docker image

First, ensure ping2 is running at <http://localhost:81/>. Then run the below commands.

    docker run --detach --env PING2_SERVER="http://localhost:81/" --publish 82:5002 henryfbp/ping3:latest
    echo "Visit http://localhost:82/ping3"

