#!/bin/bash

cd "/home/hass/.homeassistant/"
git pull
sudo sytemctl restart home-assistant.service
