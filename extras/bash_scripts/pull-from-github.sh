#!/bin/bash

cd "/home/hass/.homeassistant/"
git checkout master
git pull
sudo sytemctl restart home-assistant.service
