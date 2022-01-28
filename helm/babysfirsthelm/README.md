## start nginx helm deployment

    minikube start

    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm install nginx bitnami/nginx

    helm list

    kubectl get pod
    kubectl get deployment
    kubectl get replicaset
    kubectl get service
    
    minikube service nginx

## new helm chart

    if [ ! -d demo ]; then
        echo "Creating demo/"
        helm create demo
    else
        echo "demo/ exists, skipping"
    fi