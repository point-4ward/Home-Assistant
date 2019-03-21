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

_now=$(date +"%d_%m_%Y")
_file="backup_$_now.zip"

cd /opt
rsync -avz --delete --exclude=docker/mosquitto/mosquitto.db --exclude=docker/mariadb/* --exclude=backup_zip/* . backup_tmp/
zip -r backup_zip/$_file backup_tmp/
cd dropbox/
python dropbox_sync.py
cd /opt
rsync -avz --delete backup_zip/ /media/ext/Backups/Homeassistant/
rm -rf backup_tmp/*
rm -rf backup_tmp/.*
curl -X POST -H "Authorization: Bearer $1" $2

exit

