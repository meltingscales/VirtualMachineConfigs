#!/usr/bin/env bash

NONROOT_USER=vagrant

sudo su $NONROOT_USER

cd /home/$NONROOT_USER

mkdir -p Git

pushd Git

git clone https://github.com/philipperemy/tensorflow-1.4-billion-password-analysis
git clone https://github.com/skyblueee/sqli-labs-php7
git clone https://github.com/tuxotron/Audi_SQLi_lamp_container
git clone https://github.com/WebGoat/WebGoat
git clone https://github.com/bkimminich/juice-shop
git clone https://github.com/joaomatosf/jexboss

if [ ! -f /home/$NONROOT_USER/.ssh/id_rsa ]; then
	echo "You must create an SSH key, and you should then import it into Git! Not cloning personal repos using SSH."
	git clone https://github.com/HenryFBP/hackthebox
	git clone https://github.com/HenryFBP/autohackthebox
	git clone https://github.com/HenryFBP/VirtualMachineConfigs
	git clone https://github.com/HenryFBP/dotfiles

else
	git clone git@github.com:HenryFBP/hackthebox
	git clone git@github.com:HenryFBP/autohackthebox
	git clone git@github.com:HenryFBP/VirtualMachineConfigs
	git clone git@github.com:HenryFBP/dotfiles
fi


# bwapp and docker script
git clone https://github.com/jehy-security/bwapp
mkdir -p bwapp-docker

pushd bwapp-docker
cat > ./start-bwapp-docker.sh <<EOF
#!/usr/bin/env bash

docker run -d -p 80:80 -p 21:21 -p 8443:8443 -p 443:443 raesene/bwapp;
echo "go to http://localhost:80/install.php to see BWAPP :)"
EOF
popd #bwapp-docker

git clone https://github.com/hclproducts/AltoroJ

if [ ! -f jboss-4.0.4.GA-Patch1-installer.jar ]; then
	echo "jboss installer DNE, downloading (please wait)..."
	wget https://ayera.dl.sourceforge.net/project/jboss/JBoss/JBoss-4.0.4.GA/jboss-4.0.4.GA-Patch1-installer.jar -o jboss-4.0.4.GA-Patch1-installer.jar
else
	echo "JBoss JAR already downloaded."
fi

popd # leave ~/Git

chown -R $NONROOT_USER:$NONROOT_USER /home/$NONROOT_USER/Git
