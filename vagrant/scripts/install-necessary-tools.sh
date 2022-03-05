#!/usr/bin/env bash

# sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt update

apt install -y asciinema

# apt install -y python3.9-full
# python3.9 -m pip install pipenv poetry
# apt install -y python3.9-pip #why is this not installed by default?!

curl https://bootstrap.pypa.io/get-pip.py | python3
python3 -m pip install pipenv poetry


apt install -y firefox chromium-browser

apt install -y snap gitk
sudo snap install bashtop
sudo snap install --classic code
sudo snap install --classic gradle
sudo snap install --classic powershell

apt install -y gcc make perl ruby maven
gem install mdless

sudo snap install --classic go # we need this as we must be using at least go v1.14.1 ... apt-get gives us an older version >:(
