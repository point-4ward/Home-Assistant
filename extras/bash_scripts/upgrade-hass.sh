#!/bin/bash -x
sudo systemctl stop home-assistant.service
sudo apt-get update && sudo apt-get upgrade -y && sudo apt-get autoremove
source /srv/hass/hass_venv/bin/activate
pip3 install --upgrade homeassistant
sudo reboot
