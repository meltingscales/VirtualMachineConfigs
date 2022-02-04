# pingn

## What is this

Example of server that either asks another server for data, or serves data on its own.

## Running locally

To make 3 servers (may need to run in separate terminals), run in BASH (not fish or zsh!!)

    pipenv install

### bash

```sh
ROOT_PING=1 APP_NAME=ping1 PORT=5001                                                  pipenv run python pingn.py
            APP_NAME=ping2 PORT=5002 CHILD_URL=http://localhost:5001 CHILD_NAME=ping1 pipenv run python pingn.py
            APP_NAME=ping3 PORT=5003 CHILD_URL=http://localhost:5002 CHILD_NAME=ping2 pipenv run python pingn.py
```

### powershell

```ps1
$ROOT_PING=1 $APP_NAME=ping1 $PORT=5001                                                    pipenv run python pingn.py
             $APP_NAME=ping2 $PORT=5002 $CHILD_URL=http://localhost:5001 $CHILD_NAME=ping1 pipenv run python pingn.py
             $APP_NAME=ping3 $PORT=5003 $CHILD_URL=http://localhost:5002 $CHILD_NAME=ping2 pipenv run python pingn.py
```

### let's have fun

    bash lotsaping.sh

#### stop the fun

    ps -aux | grep pingn
    pkill -f "python pingn.py"
    rm *.log

## Build docker image

    docker build ./ --tag henryfbp/pingn:latest


### Test local docker image

TODO change this

First, ensure ping1 is running at <http://localhost:80/>. Then run the below commands.

    docker run --detach --env CHILD_URL="http://localhost:80" --publish 81:5001 henryfbp/ping2:latest
    echo "Visit http://localhost:81/ping2"

### upload to docker hub (only if you're henryfbp)

    docker login
        (le creds)
    docker push henryfbp/pingn

### Test local docker image TODO FIX IT

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
