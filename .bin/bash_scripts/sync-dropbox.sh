#!/bin/bash

#############################################################
## This script runs rsync to get everything except the log ##
## and database files from the .homeassistant directory    ##
## and copies them to a backup folder, it then sends the   ##
## contents of that folder to my dropbox account           ##
#############################################################

cd /home/homeassistant/.homeassistant/
rsync -avz --delete --exclude home-assistant.log --exclude home-assistant_v2.db*  . ../homeassistant_backup/
cd private/
python dropbox_sync.py
curl -X POST -H "Authorization: Bearer $1" $2

exit
