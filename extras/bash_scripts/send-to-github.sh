#!/bin/bash

####################################
## This script pushes my selected ##
## files to my github repo on a   ##
## new branch called 'upload'     ##
####################################

cd /home/hass/.homeassistant
git checkout -b upload
git checkout upload
git add .
git status
git commit -m "Push from local."
git push origin upload
exit