#!/bin/bash

###############################################
## This script upgrades the OS on my device, ##
## upgrades the docker containers, pulling   ##
## any config changes from Github if needed. ##
###############################################

cd /opt/docker
git fetch origin master
git reset --hard origin/master
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
docker-compose down
docker-compose pull
docker-compose up -d
docker system prune -fa
exit
