#!/bin/bash

###########################################
## This script upgrades the OS on my pi, ##
## upgrades HA then reboots the device   ##
## having pulled any config changes from ##
## Github if needed.                     ##
###########################################

cd /home/homeassistant/.homeassistant/
./update.sh
git checkout master
git branch -D upload
git fetch origin master
git reset --hard origin/master
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
source ~/srv/bin/activate
pip3 install --upgrade homeassistant
sudo reboot