#!/usr/bin/env bash

apt install asciinema

apt install -y python3-pip #why is this not installed by default?!
python3 -m pip install pipenv

apt install -y snap gitk
sudo snap install bashtop
sudo snap install --classic code
sudo snap install --classic gradle
sudo snap install --classic powershell

apt install -y gcc make perl ruby maven
gem install mdless

sudo snap install --classic go # we need this as we must be using at least go v1.14.1 ... apt-get gives us an older version >:(
