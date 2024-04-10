#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

mkdir -p Kalkulajda/DEBIAN
mkdir -p Kalkulajda/usr/bin
mkdir -p Kalkulajda/usr/local/bin
touch Kalkulajda/DEBIAN/control
echo "Package: Kalkulajda
Version: 1.0
Section: base
Priority: optional
Architecture: all
Depends: python3
Maintainer: matus.csirik@gmail.com
Description: Basic calculator." > Kalkulajda/DEBIAN/control

cp -r Pictures Kalkulajda/usr/bin/

# Copy the binary executables into the package
cp calculator Kalkulajda/usr/bin/
cp profiling Kalkulajda/usr/bin/

# Create symbolic links to the executables
ln -sf /usr/bin/calculator Kalkulajda/usr/local/bin/kalkulajda
ln -sf /usr/bin/profiling Kalkulajda/usr/local/bin/kalkulajda_p

sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-tk
sudo apt-get -y install tk-dev
pip3 install -r requirements.txt

dpkg-deb --build Kalkulajda
sudo dpkg -i Kalkulajda.deb
