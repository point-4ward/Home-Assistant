#!/bin/bash

####################################
## This script pulls my selected ##
## files to my github repo        ##
####################################

cd /home/hass/.homeassistant/
git checkout master
git pull
sudo systemctl restart home-assistant.service
