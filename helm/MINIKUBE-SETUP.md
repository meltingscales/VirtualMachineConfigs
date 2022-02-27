# useful commands

### start minikube

    minikube start --driver=docker
    minikube start

## Rancher 

### Create new Rancher container

    docker run --detach \
        --restart=unless-stopped \
        -p 80:81 -p 443:444 \
        --privileged \
        --name rancher \
        rancher/rancher:latest

### Start existing Rancher

    docker start --detach \
        --restart=unless-stopped \
        -p 80:81 -p 443:444 \
        --privileged \
        --name rancher \
        rancher/rancher:latest
    echo "now go visit https://localhost:443/"