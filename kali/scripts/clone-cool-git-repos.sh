#!/usr/bin/env bash

sudo su vagrant

cd /home/vagrant

mkdir -p Github

pushd Github

git clone https://github.com/philipperemy/tensorflow-1.4-billion-password-analysis

git clone https://github.com/skyblueee/sqli-labs-php7
git clone https://github.com/WebGoat/WebGoat

popd

chown -R vagrant:vagrant /home/vagrant/Github