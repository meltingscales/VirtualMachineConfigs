#!/usr/bin/env bash

# temporarily switch users to root to run install tasks
sudo su root

git clone https://github.com/HenryFBP/examples/ /usr/share/henryfbp-examples/
pushd /usr/share/henryfbp-examples/python3/django/orm_example/

git pull

pip3 install pipenv
pip3 install django-crispy-forms
pip3 install django

python3 -m pipenv run pip freeze > requirements.txt
python3 -m pip install requirements.txt

python3 manage.py makemigrations orm_example
python3 manage.py migrate

systemctl daemon-reload # these fail as we are in a chroot partition due to QEMU :(
systemctl enable python-orm-example
systemctl restart python-orm-example

systemctl status python-orm-example

curl http://127.0.0.1:8000/

popd