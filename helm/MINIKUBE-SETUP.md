# useful commands

## Minikube

### Start

    minikube start --driver=docker
    minikube start

## Rancher 

### Create new

    docker run --detach \
        --restart=unless-stopped \
        -p 80:81 -p 443:444 \
        --privileged \
        --name rancher \
        rancher/rancher:latest

### Restart existing 

    docker start rancher

    echo "now go visit https://localhost:443/"

### Get da creds

    docker logs rancher 2>&1 | grep "Bootstrap Password:"