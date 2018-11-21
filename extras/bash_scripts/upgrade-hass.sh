#!/bin/bash

###############################################
## This script upgrades the OS on my device, ##
## upgrades HA then reboots, having pulled   ##
## any config changes from Github if needed. ##
###############################################

cd /home/homeassistant/.homeassistant/
git checkout master
git branch -D upload
git fetch origin master
git reset --hard origin/master
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
./update_custom_ui.sh
./update_custom_text.sh
./update_hline.sh
source /srv/homeassistant/bin/activate
pip3 install --pre --upgrade homeassistant
sudo reboot
