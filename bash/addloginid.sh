#!/bin/bash
# Credit for this script goes to one of my friends, Peter.

if [[ $EUID -ne 0 ]]; then
	echo "You're not root."
	exit 1
fi

answer=Y # Yes, initially.

while [[ $answer  =~ ^[Yy]$ ]]; do
	echo "Username: "
	read username

	if id "$username" > /dev/null 2>&1; then
		echo "User exists, exiting."
		exit
	fi

	echo "First name:"
	read fname

	echo "Last name:"
	read lname

	echo "Last entry in /etc/passwd:"
	lastent="$(tail -1 /etc/passwd)"
	echo $lastent

	lastuid="$(echo $lastent | cut -d ':' -f3)"
	echo "Next available UID:"
	echo $(($lastuid + 1))

	echo "Last entry in /etc/group:"
	lastgrp="$(tail -1 /etc/group)"
	echo $lastgrp

	lastgrpnum="$(echo $lastgrp | cut -d ':' -f3)"

	echo "Next available GID:"
	echo $(($lastgrpnum + 1))

	groupadd -g "$(($lastgrpnum + 1))" $username
	echo "Group '$username' with GID '$(($lastgrpnum + 1))' created!"

	useradd $username -u "$(($lastuid + 1))" -g "$(($lastgrpnum + 1))"
	echo "User '$username' with UID '$(($lastuid + 1))' created!"

	homedir=/home/$username

	echo "Making user's home directory."
	mkdir $homedir

	echo "Setting owner of user's home dir."
	chown $username $homedir

	echo "Copying skeleton files."
	cp /etc/skel/* $homedir/

	echo "Setting password for $username."
	passwd $username

	echo "Home dir is $homedir"
	ls -dl $homedir
	ls -la $homedir/
	echo "Last entry in /etc/passwd:"
	tail -1 /etc/passwd
	echo "Last group in /etc/group:"
	tail -1 /etc/group

	echo "Make new user? (Y/N)"
	read answer
done

