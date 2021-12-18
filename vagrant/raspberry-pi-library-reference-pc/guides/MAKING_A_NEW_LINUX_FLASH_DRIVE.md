Oh no!

I deleted/formatted/lost/destroyed that flash drive in the envelope in the reference desk!

AAAAA!

# How to do it

## You will need:

- Any flash drive (doesn't matter what's on it as it will be overwritten)

- The ISO file located at `http://cdimage.ubuntu.com/lubuntu/releases/18.04/release/lubuntu-18.04.1-desktop-i386.iso`,
	- This is the Lubuntu CD image. It is what is booted off of.
	
- The program, Rufus, located at `tools\rufus-3.1.exe`.
	- This is the program which copies the ISO file over to the flash drive.

## Ok, now how do I do it?

1. Plug in the flash drive.
2. Run Rufus.
3. Under `Device`, select the drive letter that corresponds to the flash drive you plugged in.
4. Under `Boot selection`, click on the `SELECT` button and select the ISO file that you want the
   flash drive to have.
5. Click on `Start`.
6. If it asks you to download required files, click `Yes`.
7. It will tell you that an ISOHybrid image is detected.
   
   It will prompt you to either:
   
   - Write in ISO mode,
   - Write in dd mode.
   
   Select dd mode for maximum compatability.
8. You're done! Check that it boots.