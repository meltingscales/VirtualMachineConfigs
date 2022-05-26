# pingn Helm chart

See ../docker/pingn/ for the original Python app.

It's just a chain of apps that consume eachother and log some test data to a db.

## deploy

    helm upgrade pingn ./pingn/ --install
