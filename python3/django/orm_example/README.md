# How do I run this?

## Install dependencies

Run `pip install pipenv` to install a dependency manager called "pipenv".

Then, run `pipenv install --system` to install dependencies described in
`Pipfile`.

## Make and apply migrations

You only need these steps whenever you change `models.py`.

### Make migrations

You can do this by running `python manage.py makemigrations orm_example`.

### Apply migrations

Apply the migrations by running `python manage.py migrate`.

## Run it 

Run `python manage.py runserver`.