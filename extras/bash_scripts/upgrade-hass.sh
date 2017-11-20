#!/bin/bash -x

##########################################
## This script upgrades the OS on my pi,##
## upgrades HA then reboots the device  ##
##########################################

sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
source ~/bin/activate
pip3 install --upgrade homeassistant
sudo reboot