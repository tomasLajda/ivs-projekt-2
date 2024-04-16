#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Remove the installed package
sudo dpkg -r Kalkulajda

# Remove the symbolic links
rm Kalkulajda/usr/local/bin/kalkulajda
rm Kalkulajda/usr/local/bin/kalkulajda_p

# Remove the Pictures directory from /usr/bin
rm -r Kalkulajda/usr/bin/Pictures

# Remove the Kalkulajda directory if it exists
if [ -d "Kalkulajda" ]; then
    sudo rm -r Kalkulajda
fi

# Remove the Pictures directory if it exists
if [ -d "Pictures" ]; then
    sudo rm -r Pictures
fi

echo "Uninstallation completed."