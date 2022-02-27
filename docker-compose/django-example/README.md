# Django and docker-compose

stolen from <https://docs.docker.com/samples/django/>

## start docker-compose app

run dis shitttt boyee

    sudo docker-compose up

go to <https://localhost:8000/>

You should NOT see any .sqlite3 files.

## test postgresql

    sudo apt install -y pgadmin3
    pgadmin3 & 
    # connect to postgres:postgres@localhost:5432

## make migrations

    sudo docker-compose run web python manage.py makemigrations

## migrate

    sudo docker-compose run web python manage.py migrate