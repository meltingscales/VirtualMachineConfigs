#!/usr/bin/env bash

sudo dmesg | grep "Hypervisor detected" || echo "You are not in a VM! Don't run this! It will destroy your partitions!" && exit 1

echo "Resizing partition to fill the entire filesystem..."

# exit 1 # debug stop

# size of new swap, in GB
NEW_SWAP_SIZE=6 # TODO The real swap size is larger for some reason than it should be. Fix this.

# Check to see if we've already grown the main partition
if [[ -f /etc/vagrant_already_grown_main_partition ]]; then
  echo "/etc/vagrant_already_grown_main_partition exists!"
  echo "We are not going to partition. We have already."
  exit 0
fi

# turn off swap
swapoff /dev/sda5

(
echo d # delete part
echo 2 # extended part 2 which had swap in it
echo p # print part table before writing
echo w # write part table
) | sudo fdisk /dev/sda

# show partitions
lsblk

# Size of entire disk
SDA_SIZE_GB=$(lsblk /dev/sda | grep "sda " | tr -s ' ' | cut -d ' ' -f 4)
echo "Disk size is ${SDA_SIZE_GB}."

# Size of the main partition, minus 6GB for swap.
SDA_MAIN_PART_SIZE=$(expr ${SDA_SIZE_GB//G} - $NEW_SWAP_SIZE)"G"
echo "Main partition should be ${SDA_MAIN_PART_SIZE}."

# Resize /dev/sda1
(
echo resizepart # resize a partition
echo 1  # resize sda1
echo Yes
echo ${SDA_MAIN_PART_SIZE} # leave some space for swap
echo q  # quit
) | sudo parted ---pretend-input-tty /dev/sda

# make partition take up the entire space
sudo resize2fs /dev/sda1

# show partitions
lsblk

(
echo n  # create new partition
echo p  # primary partition
echo 2  # 2nd partition number
echo    # default first sector (~96GB)
echo    # default last sector (~100GB or end of disk)

echo t  # change partition type
echo 2  # partition 2 is...
echo 82 # linux swap/solaris
echo w  # write changes
) | sudo fdisk /dev/sda

# show partitions
lsblk

# format swap partition
sudo mkswap /dev/sda2

# enable swap
sudo swapon /dev/sda2

# append mount command to /etc/fstab
echo "# AUTOMATICALLY GENERATED line by kali-vagrant partition resizing script" >> /etc/fstab
echo "/dev/sda2             swap            swap            default          0   0" >> /etc/fstab

# This will error if we've fucked up /etc/fstab
sudo mount -a

# record the fact that we've grown the main partition and DO NOT do it again
sudo touch /etc/vagrant_already_grown_main_partition
