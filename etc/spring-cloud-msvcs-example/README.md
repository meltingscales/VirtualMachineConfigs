# Spring Cloud Microservices Example

taken from amigoscode with <3

- <https://www.youtube.com/watch?v=p485kUNpPvE>
- <https://github.com/amigoscode/microservices>

## docker (for le database)

    docker-compose up -d
    docker-compose ps
    docker-compose logs -f

Then visit <http://localhost:5050/> to view PGAdmin

## issues

### Invalid interpolation format

Your `docker-compose` version is probably old. Update with a binary from https://github.com/docker/compose/releases
