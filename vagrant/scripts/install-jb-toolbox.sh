#!/bin/bash

JBTBURL=https://download-cdn.jetbrains.com/toolbox/jetbrains-toolbox-1.21.9712.tar.gz

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