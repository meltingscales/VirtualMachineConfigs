#!/usr/bin/env bash

NONROOT_USER=vagrant

apt install -y fish
echo 'vagrant' | chsh vagrant -s /usr/bin/fish

curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install > omf-install.fish
chmod +x omf-install.fish
sudo -u $NONROOT_USER fish -c "./omf-install.fish --noninteractive --yes; or echo 'omf install either failed or omf is already installed.'"

rm ./omf-install.fish

# can replace this with whatever theme you want...
sudo -u $NONROOT_USER fish -c "omf install batman"
sudo -u $NONROOT_USER fish -c "omf theme batman"
