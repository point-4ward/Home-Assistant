#!/bin/bash

#####################################
## This script pulls my selected   ##
## files to my github repo, and    ##
## treats them as the 'master copy ##
#####################################

cd /home/hass/.homeassistant/
git checkout master
git branch -D upload
git fetch origin master
git reset --hard origin/master
sudo systemctl restart home-assistant.service