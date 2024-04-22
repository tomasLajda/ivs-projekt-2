#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

# Remove the installed package
dpkg -r Kalkulajda

# Remove the symbolic links
rm /usr/local/bin/kalkulajda
rm /usr/local/bin/kalkulajda_stddev

# Remove the kalkulajda.sh script and the calculator binary from /usr/bin
rm /usr/bin/kalkulajda.sh
rm /usr/bin/calculator

# Remove the Pictures directory from /usr/bin
rm -r /usr/bin/Pictures

# Remove the Kalkulajda directory if it exists
if [ -d "Kalkulajda" ]; then
    rm -r Kalkulajda
fi

# Remove the Pictures directory if it exists
if [ -d "Pictures" ]; then
    rm -r Pictures
fi

rm Kalkulajda.deb
rm installer.sh
rm kalkulajda.sh
rm uninstall.sh
rm requirements.txt
rm calculator
rm profiling
rmdir ../installer
echo "Uninstallation completed."
