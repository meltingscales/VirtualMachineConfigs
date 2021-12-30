#!/usr/bin/env bash

NONROOT_USER=vagrant
SSH_KEY_LOCATION=/home/vagrant/.ssh/id_rsa
SSH_PUBKEY_LOCATION=$SSH_KEY_LOCATION.pub

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

apt-get install -y lynx gedit

# must run as vagrant
su - vagrant <<MARKER
    if [[ ! -d ~/Git/ ]]; then
        mkdir ~/Git/
    fi

    pushd ~/Git/
        git config --global pull.rebase false
        git clone git@github.com:HenryFBP/hackthebox.git
        git clone git@github.com:HenryFBP/examples.git
        git clone git@github.com:HenryFBP/vagrantpackerfiles.git
        git clone git@github.com:danielmiessler/SecLists
    popd
MARKER

printf "lol hello, we are done\n"