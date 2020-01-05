#!/usr/bin/env bash

set -e

INSTALL=${INSTALL:-yum install -y}

log() {
	echo -e "\033[34m[bootstrapper] $* \033[0m"
}

if [ "$EUID" -ne 0 ] ; then 
	log Escalating privileges..
	sudo "$0"
	exit 0
fi

log Installing OpenVAS.

export NON_INT=yes
wget -q -O - http://www.atomicorp.com/installers/atomic |sh
yum upgrade -y
$INSTALL openvas
yum clean all

log Now 'vagrant ssh', 'sudo -i' and run 'openvas-setup'.
