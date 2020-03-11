# Packer

## ARM images

See <https://github.com/mkaczanowski/packer-builder-arm> on how to install the builder for ARM.

`packer-builder-arm` plugin must be built using Go and then stored under `/usr/bin/packer-builder-arm`.  
Make sure it's executable!

You need Linux, QEMU for this and a 64-bit processor with virtualization.

## Commands

    time -v sudo packer build raspberrypi/raspbian.json
