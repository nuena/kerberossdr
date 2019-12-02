#!/bin/bash
#
# Debian-Installation script that implements all commands found in the README.md ... nothing special.

# Check Python version first: will run into issues if < 3.6:
echo "Please verify manually that the python version is at least 3.6!"
python3 --version

read -p "Is the version number OK and do you want to continue? " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

sudo apt update
sudo apt install \
   python3-pip \
   python3-pyqt4 \
   build-essential \
   gfortran \
   libatlas3-base \
   libatlas-base-dev \
   python3-dev \
   python3-setuptools \
   libffi6 \
   libffi-dev \
   python3-tk \
   pkg-config \
   libfreetype6-dev \
   php7.2-cli

sudo apt remove python3-numpy


pip3 install numpy
pip3 install matplotlib
pip3 install scipy
pip3 install cairocffi
pip3 install pyapril
pip3 install pyargus
pip3 install pyqtgraph
pip3 install peakutils
pip3 install bottle
pip3 install paste
 

sudo apt-get install libusb-1.0-0-dev git cmake
git clone https://github.com/rtlsdrblog/rtl-sdr-kerberos
cd rtl-sdr-kerberos
mkdir build
cd build
cmake ../ -DINSTALL_UDEV_RULES=ON
make
sudo make install
sudo cp ../rtl-sdr.rules /etc/udev/rules.d/
sudo ldconfig
echo 'blacklist dvb_usb_rtl28xxu' | sudo tee --append /etc/modprobe.d/blacklist-dvb_usb_rtl28xxu.conf

