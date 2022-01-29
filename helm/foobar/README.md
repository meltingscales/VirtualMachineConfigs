# Helm chart "foobar"

Decided this is going to be a GitLab helm chart. Because why not.

## deploy

    minikube start
    helm install gitlab-test foobar/

## redeploy

    helm upgrade gitlab-test foobar/

## debug

    kubectl logs svc/gitlab-test-foobar

## uninstall

    helm uninstall gitlab-test