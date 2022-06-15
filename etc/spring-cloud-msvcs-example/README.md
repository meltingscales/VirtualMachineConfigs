# Spring Cloud Microservices Example

taken from amigoscode with <3

- <https://www.youtube.com/watch?v=p485kUNpPvE>
- <https://github.com/amigoscode/microservices>

## Running

    todo lol

2.  Manually create the `customer` database using PGAdmin

## docker (for le database)

    docker-compose up -d
    # optional below
    docker-compose ps
    docker-compose logs -f

Then visit <http://localhost:5050/> to view PGAdmin

## issues

### Invalid interpolation format

Your `docker-compose` version is probably old. Update with a binary from <https://github.com/docker/compose/releases>
