#!/bin/sh

# Check if the script is run as root
if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

apt-get update
apt-get install python3-pip
apt-get install python3-tk
apt-get install tk-dev
pip3 install -r requirements.txt

mkdir -p Kalkulajda/DEBIAN
mkdir -p Kalkulajda/usr/bin
touch Kalkulajda/DEBIAN/control
echo "Package: Kalkulajda
Version: 1.0
Section: base
Priority: optional
Architecture: all
Depends: python3
Maintainer: Matúš Csirik <matus.csirik@gmail.com>
Description: Basic calculator." > Kalkulajda/DEBIAN/control

cp -r Pictures /usr/bin

# Create the kalkulajda.sh wrapper script
touch kalkulajda.sh
echo "#!/bin/sh
cd \"\$(dirname \"\$0\")\"
./calculator" > kalkulajda.sh
chmod +x kalkulajda.sh
mv kalkulajda.sh /usr/bin/

# Move the binary executables into the package
mv calculator Kalkulajda/usr/bin/
mv profiling Kalkulajda/usr/bin/

# Assign the executable permissions to the binaries and the wrapper script
chmod +x Kalkulajda/usr/bin/calculator
chmod +x Kalkulajda/usr/bin/profiling
chmod +x /usr/bin/kalkulajda.sh

# Create symbolic links to the executables
ln -sf /usr/bin/kalkulajda.sh Kalkulajda/usr/bin/kalkulajda
ln -sf /usr/bin/profiling Kalkulajda/usr/bin/kalkulajda_p

dpkg-deb --build Kalkulajda
dpkg -i Kalkulajda.deb

# Clean up the Kalkulajda.deb file
rm Kalkulajda.deb
