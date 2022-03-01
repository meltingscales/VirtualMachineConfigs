# pingn

## What is this

Example of server that either asks another server for data, or serves data on its own.

## Running locally

To make 3 servers (may need to run in separate terminals), run in BASH (not fish or zsh!!)

    pipenv install

## test db

Can run this to connect to Docker PostgreSQL.

    psql -h localhost -U postgres pingn 
        \dt+
        SELECT * FROM logs;

### bash

```shell
ROOT_PING=1 APP_NAME=ping1 PORT=5001                                                  PSQL_HOST=localhost  pipenv run python -m pingn
            APP_NAME=ping2 PORT=5002 CHILD_URL=http://localhost:5001 CHILD_NAME=ping1                      pipenv run python -m pingn
            APP_NAME=ping3 PORT=5003 CHILD_URL=http://localhost:5002 CHILD_NAME=ping2                      pipenv run python -m pingn
```

### powershell

```powershell
$env:ROOT_PING=1; $env:APP_NAME="ping1"; $env:PORT=5001;                                                                  pipenv run python -m pingn
                  $env:APP_NAME="ping2"; $env:PORT=5002; $env:CHILD_URL="http://localhost:5001"; $env:CHILD_NAME="ping1"; pipenv run python -m pingn
                  $env:APP_NAME="ping3"; $env:PORT=5003; $env:CHILD_URL="http://localhost:5002"; $env:CHILD_NAME="ping2"; pipenv run python -m pingn
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

Note you can remove `--detach` or run `docker logs <CONTAINER>` to get logs.

```shell
docker rm pingnpg ping1 ping2 ping3 ping4 -f
docker network rm pingnnet

# this is necessary -- docker's default network does not allow the containers to communicate!!
docker network create pingnnet

docker run --name pingnpg       --hostname pingnpg  --publish 5432:5432 --env POSTGRES_PASSWORD=postgres --detach postgres 
docker run --name ping1         --hostname ping1    --publish 81:5000   --env ROOT_PING=1 --env APP_NAME=ping1                                                          --env PORT=5000 --env PSQL_HOST=pingnpg --detach henryfbp/pingn:latest
docker run --name ping2         --hostname ping2    --publish 82:5000   --env ROOT_PING=0 --env APP_NAME=ping2 --env CHILD_URL=http://ping1:5000 --env CHILD_NAME=ping1 --env PORT=5000 --detach henryfbp/pingn:latest
docker run --name ping3         --hostname ping3    --publish 83:5000   --env ROOT_PING=0 --env APP_NAME=ping3 --env CHILD_URL=http://ping2:5000 --env CHILD_NAME=ping2 --env PORT=5000 --detach henryfbp/pingn:latest
docker run --name ping4         --hostname ping4    --publish 84:5000   --env ROOT_PING=0 --env APP_NAME=ping4 --env CHILD_URL=http://ping3:5000 --env CHILD_NAME=ping3 --env PORT=5000 --detach henryfbp/pingn:latest

docker network connect pingnnet pingnpg
docker network connect pingnnet ping1
docker network connect pingnnet ping2
docker network connect pingnnet ping3
docker network connect pingnnet ping4

echo "Visit http://localhost:84/ping4"
```

### upload to docker hub (only if you're henryfbp)

    docker login
        (le creds)
    docker push henryfbp/pingn

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

## TODO

- bitnami postgresql chart
