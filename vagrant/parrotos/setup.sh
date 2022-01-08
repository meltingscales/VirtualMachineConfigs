#!/usr/bin/env bash

NONROOT_USER=vagrant
SSH_KEY_LOCATION=/home/vagrant/.ssh/id_rsa
SSH_PUBKEY_LOCATION=$SSH_KEY_LOCATION.pub

EMAIL="HenryFBP@gmail.com"
NAME="Henry Post"

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Try 'sudo $0'."
   exit 1
fi

if [[ ! -f $SSH_KEY_LOCATION ]]; then
    echo "Please generate or import an SSH key at '$SSH_KEY_LOCATION'.
This is required for cloning Git repositories.
Make sure to then import '$SSH_PUBKEY_LOCATION' into GitHub."
    exit 1
fi

apt-get update

apt-get install -y lynx gedit fish iftop


which docker # if exit code is nonzero, then it is not a command.
if [ "$?" -eq "1" ]; then
    # required to add docker
    sudo apt-get install \
        ca-certificates \
        curl \
        gnupg \
        lsb-release

    # add docker GPG key
    curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    # add docker stable repo
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
    $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    apt update

    # install docker repos
    apt install -y docker-ce docker-ce-cli containerd.io
else
    echo "Docker is already installed."
    which docker
fi

# install jb toolbox
curl https://raw.githubusercontent.com/HenryFBP/VagrantPackerFiles/master/vagrant/scripts/install-jb-toolbox.sh | sudo bash

pip3 install pipenv
pip3 install updog

# unzip rockyou.txt wordlist
if [[ ! -f /usr/share/wordlists/rockyou.txt ]]; then
    pushd /usr/share/wordlists/
        gunzip rockyou.txt.gz
    popd
fi

# must run as vagrant
su --shell=/bin/bash - $NONROOT_USER <<MARKER
    if [[ ! -d ~/Git/ ]]; then
        mkdir ~/Git/
    fi

    pushd ~/Git/
        git config --global pull.rebase false
        git config --global user.email $EMAIL
        git config --global user.name $NAME

        git clone git@github.com:HenryFBP/hackthebox.git
        git clone git@github.com:HenryFBP/dotfiles.git
        git clone git@github.com:HenryFBP/autohackthebox.git
        git clone git@github.com:HenryFBP/examples.git
        git clone git@github.com:HenryFBP/VagrantPackerFiles.git
        git clone git@github.com:danielmiessler/SecLists
        git clone git@github.com:andrew-d/static-binaries
        git clone https://github.com/HenryFBP/CVE-2021-3129_exploit
    popd
MARKER

printf "lol hello, we are done\n"