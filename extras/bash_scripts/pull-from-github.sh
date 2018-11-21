#!/bin/bash

######################################
## This script pulls my selected    ##
## files from my Github repo, and   ##
## treats them as the 'master' copy ##
######################################

cd /home/homeassistant/.homeassistant/
git checkout master
git branch -D upload
git fetch origin master
git reset --hard origin/master
sudo systemctl restart home-assistant@homeassistant.service
