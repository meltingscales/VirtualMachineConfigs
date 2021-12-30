#!/usr/bin/env bash

SSH_KEY_LOCATION=/home/vagrant/.ssh/id_rsa

if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Try 'sudo $0'."
   exit 1
fi

if [[ ! -f $SSH_KEY_LOCATION ]]; then
    echo "Please generate or import an SSH key at '$SSH_KEY_LOCATION' with 'ssh-keygen'. 
This is required for cloning Git repositories.
After doing so, make sure to import it into GitHub."
    exit 1
fi


apt-get update

if [[ ! -d ~/Git/ ]]; then
    mkdir ~/Git/
fi


pushd ~/Git/
    git clone git@github.com:HenryFBP/hackthebox.git
    git clone git@github.com:HenryFBP/examples.git
popd

printf "lol hello\n"