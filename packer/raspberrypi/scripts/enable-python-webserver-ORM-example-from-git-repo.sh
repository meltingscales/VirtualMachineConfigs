#!/usr/bin/env bash

# temporarily switch users to root to run install tasks
sudo su root

git clone https://github.com/HenryFBP/examples/ /usr/share/henryfbp-examples/ || true
pushd /usr/share/henryfbp-examples/

git pull

pip install pipenv
pipenv install --system

python manage.py makemigrations orm_example
python manage.py migrate