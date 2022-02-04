#!/usr/bin/env bash

apt install -y fish
echo 'vagrant' | chsh vagrant -s /usr/bin/fish

curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install > omf-install.fish
chmod +x omf-install.fish
./omf-install.fish --noninteractive --yes || echo 'omf install either failed or omf is already installed.'
rm ./omf-install.fish

# can replace this with whatever theme you want...
fish -c "omf install batman"
fish -c "omf theme batman"
