#!/bin/bash

#################################################
## This script runs the dropbox_sync.py script ##
## as I could not get it to run directly!      ##
#################################################

cd /home/homeassistant/.homeassistant/
rsync -avz --exclude home-assistant.log --exclude home-assistant_v2.db  . ../homeassistant_backup/
cd private/
python dropbox_sync.py
exit
