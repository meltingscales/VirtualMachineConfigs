## Running

    pipenv install
    pipenv run python ping1.py

## Build docker image

    docker build ./ --tag ping1:latest

### test

    docker run -d -p 5000:8080 ping1:latest
    echo "Visit http://localhost:8080/ping1"