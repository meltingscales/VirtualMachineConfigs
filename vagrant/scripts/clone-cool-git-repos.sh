#!/usr/bin/env bash

# if not set
if [ -z $NONROOT_USER ]; then
	NONROOT_USER=vagrant
fi

GITFLAGS=--recurse-submodules

sudo su $NONROOT_USER

cd /home/$NONROOT_USER

mkdir -p Git

pushd Git

git clone $GITFLAGS https://github.com/philipperemy/tensorflow-1.4-billion-password-analysis
git clone $GITFLAGS https://github.com/skyblueee/sqli-labs-php7
git clone $GITFLAGS https://github.com/tuxotron/Audi_SQLi_lamp_container
git clone $GITFLAGS https://github.com/WebGoat/WebGoat
git clone $GITFLAGS https://github.com/bkimminich/juice-shop
git clone $GITFLAGS https://github.com/joaomatosf/jexboss

git clone $GITFLAGS git@github.com:HenryFBP/adventofcode
git clone $GITFLAGS git@github.com:HenryFBP/examples
git clone $GITFLAGS git@github.com:HenryFBP/hackthebox
git clone $GITFLAGS git@github.com:HenryFBP/autohackthebox
git clone $GITFLAGS git@github.com:HenryFBP/VirtualMachineConfigs
git clone $GITFLAGS git@github.com:HenryFBP/dotfiles
git clone $GITFLAGS git@github.com:HenryFBP/books


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
