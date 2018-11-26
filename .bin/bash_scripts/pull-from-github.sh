#!/bin/bash

######################################
## This script pulls my selected    ##
## files from my Github repo, and   ##
## treats them as the 'master' copy ##
######################################

cd /opt/docker
git fetch origin master
git reset --hard origin/master
#TODO - restart the container
exit
