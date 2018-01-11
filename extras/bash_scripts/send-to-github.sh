#!/bin/bash

####################################
## This script pushes my selected ##
## files to my github repo on a   ##
## new branch called 'upload'     ##
####################################

cd /home/hass/.homeassistant
git add .
git status
git checkout -b upload
git commit -m "$1"
git push origin upload
exit
