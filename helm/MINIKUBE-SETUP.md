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

    echo "now go visit https://localhost:443/"

### Restart existing 

    docker start rancher

    echo "now go visit https://localhost:443/"

### Get da creds

    docker logs rancher 2>&1 | grep "Bootstrap Password:"

Change the default password and make sure to write it down somewhere.

If you forget your Rancher password, run this:

    docker exec --interactive --tty rancher reset-password

Once you log in, download the kubeconfig yaml file, and put it in `~/.kube/config`.

Then run

    kubectl get node --insecure-skip-tls-verify

And you should see a control plane node.