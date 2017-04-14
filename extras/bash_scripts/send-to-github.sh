#!/bin/bash

###################################
## This script pushes my selected ##
## files to my github repo        ##
####################################

cd /home/hass/.homeassistant
git add .
git status
echo -n "Enter the Description for the Change: " [Minor Update]
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin master
exit
