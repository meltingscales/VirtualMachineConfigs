# How do I boot into Linux?

1. Get the Lubuntu flash drive from the reference desk's money drawer
2. Plug the flash drive into 

# Why do I need to do this?

- Linux has two things that Windows doesn't natively support:

  1. It supports the ext4 filesystem.
  
	 This just means that Linux knows how to manipulate and interpret the filesystem that the
	 raspberry pi uses.

  2. It has `dd`.
  
     `dd` is a tool that copies the contents of disks around.

# FAQ/Frequent problems

## Where's the boot menu?
- Usually, to access the boot menu, you must press one of the function keys while the computer
  is booting up.
	  
  Common keys are `F8`, `F12`, and `DELETE`.

## The USB drive doesn't show up!
- On newer PCs that have newer motherboards, there is a new system of booting into OSes that is
  called 'UEFI boot'.
	  
  If your motherboard is set up to use UEFI boot mode instead of 'legacy boot', you will likely
  need to change it to use legacy boot mode.

## The option shows up, I select it, but it says 'Boot Failed' or 'Booting from medium failed', etc

- Make sure that the only removable storage medium inserted is the Lubuntu drive.