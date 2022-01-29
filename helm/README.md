## useful commands

### start minikube

    minikube start --driver=docker
    minikube start

### start rancher

    docker run -d --restart=unless-stopped \
        -p 80:81 -p 443:444 \
        --privileged \
        rancher/rancher:latest

    echo "now go visit https://localhost:444/"