# Packer

## ARM images

You need Linux, QEMU for this and a 64-bit processor with virtualization.

You need to install these packages:

    sudo apt-get install git unzip qemu-user-static e2fsprogs dosfstools bsdtar 
    
If `bsdtar` fails then install `libarchive-tools`.

You may need to download the Go binary manually if `apt` installs a version older than 1.14.1:
<https://golang.org/doc/install#install>

See <https://github.com/mkaczanowski/packer-builder-arm> on how to install the builder for ARM.

`packer-builder-arm` plugin must be built using Go 1.14.1 and then stored under `/usr/bin/packer-builder-arm`.  
Make sure it's executable!

## Raspberry Pi

### Building

    mkdir -p images_output
    sudo packer build raspberrypi/raspbian.json
    
Here's a tip. Have a raspberry Pi on hand to load these image files onto, because if your build
command starts to take long, you can test commands on the RPi and then just add them into this 
script once they work, because you can test them without having to wait if you have a physical RPi. 

### Testing built image

See <https://azeria-labs.com/emulate-raspberry-pi-with-qemu/>

I have not gotten this to work. This may be very hard.
