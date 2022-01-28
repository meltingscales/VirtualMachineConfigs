#!/usr/bin/env bash

# packer-builder-arm setup, from <https://github.com/mkaczanowski/packer-builder-arm>
which packer-builder-arm
if [ ! "$?" -eq "0" ]; then # if exit code is nonzero, it is not a command  
    echo "Installing packer-builder-arm from source, as it does not exist on path!"
    pushd /tmp/
    git clone https://github.com/mkaczanowski/packer-builder-arm
    cd packer-builder-arm
    go mod download
    go build
    chmod +x ./packer-builder-arm
    sudo cp ./packer-builder-arm /usr/bin/
    sudo packer build boards/odroid-u3/archlinuxarm.json || (echo "Failed! See packer-builder-arm section and fix!")
    popd    
else
    echo "'/usr/bin/packer-builder-arm' already exists!"
fi
# end of packer-builder-arm setup
