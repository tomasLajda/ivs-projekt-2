#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Remove the installed package
sudo dpkg -r Kalkulajda

# Remove the symbolic links
sudo rm /usr/local/bin/kalkulajda
sudo rm /usr/local/bin/kalkulajda_p

# Remove the kalkulajda.sh script and the calculator binary from /usr/bin
sudo rm /usr/bin/kalkulajda.sh
sudo rm /usr/bin/calculator

# Remove the Pictures directory from /usr/bin
sudo rm -r /usr/bin/Pictures

# Remove the Kalkulajda directory if it exists
if [ -d "Kalkulajda" ]; then
    sudo rm -r Kalkulajda
fi

# Remove the Pictures directory if it exists
if [ -d "Pictures" ]; then
    sudo rm -r Pictures
fi

rm Kalkulajda.deb
rm installer.sh
rm uninstall.sh
rm requirements.txt
rm calculator
rm profiling

echo "Uninstallation completed."