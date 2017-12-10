#!/bin/bash

###################################
## This script pushes my selected ##
## files to my github repo        ##
####################################

cd /home/hass/.homeassistant
git checkout -b upload
git checkout upload
git add .
git status
echo -n "Enter the Description for the Change: "
read CHANGE_MSG
git commit -m "${CHANGE_MSG}"
git push origin upload
exit
