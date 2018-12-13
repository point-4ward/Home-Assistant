#!/bin/bash

##############################################################
##                                                          ##
## This script runs rsync to get everything except database ##
## files from the /opt directory and copies them to the     ##
## /opt/backup directory before zipping them to an archive. ##
##                                                          ##
## It then sends the archive file to my dropbox account     ##
##                                                          ##
##############################################################

_now=$(date +"%m_%d_%Y")
_file="backup_$_now.zip"

cd /opt
rsync -avz --delete --exclude=docker/mosquitto/mosquitto.db --exclude=docker/mariadb/* . backup/
zip -r backup/zip/$_file backup/
cd dropbox/
python dropbox_sync.py
rm -rf backup/*
curl -X POST -H "Authorization: Bearer $1" $2

exit
