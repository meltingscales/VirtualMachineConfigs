#!/usr/bin/env bash

if ! command -v jetbrains-toolbox &> /dev/null
then
    echo "jetbrains-toolbox could not be found, downloading"
    pushd /tmp/
        curl -L https://download.jetbrains.com/toolbox/jetbrains-toolbox-1.26.1.13138.tar.gz --output toolbox.tar.gz

        tar -xf toolbox.tar.gz

        pushd ./jetbrains-toolbox-*/
            cp jetbrains-toolbox /usr/local/bin/
        popd
    popd
else
    echo "jetbrains toolbox already installed." 
fi