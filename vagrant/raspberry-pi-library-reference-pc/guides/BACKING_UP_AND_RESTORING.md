NOTE: You can only run `dd` on a *nix system. See the money drawer for Lubuntu on a USB.

NOTE 2: Make sure you got enough space! Might take up 8GB-32GB, worst-case.

NOTE 2.5: `dd` is sometimes called Disk Destroy. It's powerful! Use with caution. Double-check!

NOTE 2.75: `dd` actually stands for Data Duplicator.

NOTE 3: Will take from 10-20 minutes! Doesn't show progress, so MAKE SURE your paths are correct!

See [this link](https://www.raspberrypi.org/forums/viewtopic.php?t=46911) for more information.

# To back up an SD card to a file:

## YOU WILL NEED:

- The SD card, and a reader.
- A PC running linux.
- A place to store the image of the SD card, preferrably another flash drive.

## RUN THIS COMMAND IN TERMINAL:


	sudo dd bs=4M if=/dev/mmcblk0 | gzip > /home/your_username/raspberry_pi_image-`date +%y%m%d`.gz

	
A NOTE: You MUST substitute `/home/your_username/` for wherever your other flash drive is mounted.
		Usually, it's at `/media/lubuntu/1357-9BDF/` or some similarly-named place.

## BREAKDOWN OF COMMAND:

So, `dd ... if=/dev/mmcblk0` is using `/dev/mmcblk0` as a source for data. `if` stands for 'input file'.

IMPORTANT NOTE: `dev/mmcblk0` is specific to the reference computer behind me and its SD card
				reader. Please double-check that that drive is the correct one! It may not
				exist on other computers.


The `|` symbol 'pipes' the output of that `dd` command into `gzip`, a program that compresses
our otherwise 32GB image into a 3GB image.

The `>` symbol after `gzip` redirects the output of the `gzip` command into whatever file is after
that symbol.

So, in english, the command would be:

	data_duplicate MY_SD_CARD into ZIPPER which zips into MY_FILE-18-08-01.gz

# To restore the backup onto an SD card:

## YOU WILL NEED:

- The SD card, and a reader.
- A PC running linux.
- A place to provide the image of the SD card, preferrably another flash drive.

## RUN THIS COMMAND IN TERMINAL:


	sudo gzip -dc /home/your_username/image.gz | sudo dd bs=4M of=/dev/mmcblk0

	
A NOTE: You MUST substitute `/home/your_username/` for wherever your other flash drive is mounted.
		Usually, it's at `/media/lubuntu/1357-9BDF/` or some similarly-named place.
	
## BREAKDOWN OF COMMAND:

Funnily enough, this command just looks like the first one, but in reverse.

Here, we start by unzipping our `.gz` file and we use the `|` character to 'pipe' the output
into the `dd` command.

We then tell `dd` to output the file to `/dev/mmcblk0`.

IMPORTANT NOTE: `dev/mmcblk0` is specific to the reference computer behind me and its SD card
				reader. Please double-check that that drive is the correct one! It may not
				exist on other computers.


Again, in english, the command would be:

	unzip MY_FILE-18-08-01.gz into data_duplicator onto MY_SD_CARD
