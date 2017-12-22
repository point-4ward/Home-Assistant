#!/bin/bash -x

##########################################
## This script upgrades the OS on my pi,##
## upgrades HA then reboots the device  ##
##########################################

cd /home/hass/.homeassistant/
git checkout master
git branch -D upload
git fetch origin master
git reset --hard origin/master
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
source ~/srv/bin/activate
pip3 install --upgrade homeassistant
sudo reboot
