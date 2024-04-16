#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Remove the installed package
sudo dpkg -r Kalkulajda

# Remove the symbolic links
rm /usr/local/bin/kalkulajda
rm /usr/local/bin/kalkulajda_p

# Remove the Pictures directory from /usr/bin
rm -r /usr/bin/Pictures

echo "Uninstallation completed."