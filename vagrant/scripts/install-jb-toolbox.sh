#!/usr/bin/env bash

JBTBURL=https://download-cdn.jetbrains.com/toolbox/jetbrains-toolbox-1.21.9712.tar.gz
TOOLLOC=/bin/jetbrains-toolbox

if [[ ! -f $TOOLLOC ]]; then
    pushd /tmp/

        curl $JBTBURL > toolbox.tar.gz

        gunzip toolbox.tar.gz
        tar -xf toolbox.tar

        pushd jetbrains-toolbox-*/
            chmod +x jetbrains-toolbox
            mv jetbrains-toolbox /bin/
        popd
    popd

    jetbrains-toolbox &
else
    echo "Already exists: $TOOLLOC"
fi