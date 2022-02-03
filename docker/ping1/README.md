# Running

    pipenv install
    pipenv run python ping1.py

# Build docker image

    docker build ./ --tag ping1:latest

## test

    docker run -d -p 80:5000 ping1:latest
    echo "Visit http://localhost:80/ping1"

## stop the test

    docker ps
    docker stop <id>

# Notes

https://sourcery.ai/blog/python-docker/