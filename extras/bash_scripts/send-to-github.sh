#!/bin/bash

####################################
## This script pushes my selected ##
## files to my github repo on a   ##
## new branch called 'upload'     ##
####################################

cd /home/homeassistant/.homeassistant
git add .
git checkout -b upload
git commit -m "$1"
git push origin upload
exit
