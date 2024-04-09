#!/bin/sh
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
cp calculator.py Kalkulajda/usr/bin/
chmod +x Kalkulajda/usr/bin/calculator.py
cp mathlib.py Kalkulajda/usr/bin/
cp help_menu.py Kalkulajda/usr/bin/
cp -r Pictures Kalkulajda/usr/bin/
cp profiling.py Kalkulajda/usr/bin/
chmod +x Kalkulajda/usr/bin/profiling.py

# Create a shell script to run the Python script
echo "#!/bin/sh
python3 /usr/bin/calculator.py" > Kalkulajda/usr/bin/run_calculator.sh
chmod +x Kalkulajda/usr/bin/run_calculator.sh

# Create symbolic links to the shell script
ln -sf /usr/bin/run_calculator.sh Kalkulajda/usr/local/bin/kalkulajda

sudo apt-get -y update
sudo apt-get -y install python3-pip
sudo apt-get -y install python3-tk
sudo apt-get -y install tk-dev
pip3 install -r requirements.txt
dpkg-deb --build Kalkulajda