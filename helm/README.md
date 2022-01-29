## useful commands

### start minikube

    minikube start --driver=docker
    minikube start

### start rancher

    docker run -d --restart=unless-stopped \
  -p 80:80 -p 443:443 \
  --privileged \
  rancher/rancher:latest
