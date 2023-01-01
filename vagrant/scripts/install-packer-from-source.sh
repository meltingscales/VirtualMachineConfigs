#!/usr/bin/env bash

VERSION=v1.7.8

# packer setup, from source
which packer
if [ ! "$?" -eq "0" ]; then # if exit code is nonzero, it is not a command  
    echo "Installing packer from source, as it does not exist on path!"
    pushd /tmp/
    mkdir -p /tmp/packer-setup/
    pushd /tmp/packer-setup/
    wget https://github.com/hashicorp/packer/archive/refs/tags/$VERSION.zip
    unzip $VERSION.zip
    cd ./packer-*/
    echo "Time to wait for go to compile packer binary!"
    go mod download
    mkdir -p ./bin/
    go build -o bin/packer ./
    chmod +x bin/packer
    mv bin/packer /bin/packer

    ls -lash /bin/packer
    packer -v
    popd # to /tmp
    popd # to whatever before
else
    echo "packer already exists."
fi
