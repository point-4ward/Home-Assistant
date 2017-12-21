#!/bin/bash

####################################
## This script pulls my selected ##
## files to my github repo        ##
####################################

cd /home/hass/.homeassistant/
git checkout master
git branch -D upload
git fetch origin
git reset --hard origin/master
sudo systemctl restart home-assistant.service
