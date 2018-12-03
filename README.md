[![CircleCI](https://circleci.com/gh/mf-social/Home-Assistant.svg?style=shield)](https://circleci.com/gh/mf-social/Home-Assistant) [![LastCommit](https://img.shields.io/github/last-commit/mf-social/Home-Assistant.svg?color=blue&style=plasticr)](https://github.com/mf-social/Home-Assistant/commits/master) [![GitHub stars](https://img.shields.io/github/stars/mf-social/Home-Assistant.svg)](https://github.com/mf-social/Home-Assistant/stargazers) [![GitHub issues](https://img.shields.io/github/issues/mf-social/Home-Assistant.svg)](https://github.com/mf-social/Home-Assistant/issues) [![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/) [![contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg?style=flat)](https://github.com/mf-social/Home-Assistant/pulls) [![Uptime Robot status](https://img.shields.io/uptimerobot/status/m781496781-e11cc3f52039d8549430a954.svg)](https://uptimerobot.com/) [![Buy Me A Beer](https://img.shields.io/badge/BuyMeABeer-Paypal-blue.svg)](https://www.paypal.me/marcforth)

[What do these badges all mean?](.bin/github_resources/readme_files/badges.md)

# Changes are happening at Chateau mf_social!!  This repo is being reorganised, please bear with me whilst I get the README's caught up and get the Wiki written!!


# My Home Assistant setup:

This is my current Home Automation setup, based on Homeassistant, running in docker.  This repo contains copies of non-sensitive configuration files for the containers I am using.  This is my live system as it is running in my house at the moment.  I am currently tracking the beta channel of Homeassistant releases.  Below you will find some explanatory notes, and the [Wiki](https://github.com/mf-social/Home-Assistant/wiki) explains exactly what this repo contains and how to create a system like mine from scratch...


## What Software makes up your Home Automation System?

<details><summary>On my host system I have a few bash scripts that run mainanence and git operations, but the majority of the system is run in docker containers.  Expand to read more.</summary>
<p>

**My docker stack contains...**

Homeassistant - an open source Home Automation system that can communicate with many IOT and web based services to automate my home.

Mosquitto - an MQTT server that enables IOT devices to communicate with each other.

MariaDB - a database that homeassistant uses to record everything that is going on.

MaryTTS - a local Text-To-Speech engine that lets Homeassistant speak to us at home.

Syncthing - a peer-to-peer file synchronization application that allows me to edit and backup my configuration files on a remote device.

Dropbox - an online storage system for full off-site backups of my config.

Portainer - a graphical manager for the docker stack

Organizr - a webpage that you run on your server to help put all your services into one webpage.  This container also contains a nginx reverse proxy that directs web traffic to the correct container.
</p>
</details>


[And here's how it looks.](.bin/github_resources/readme_files/screenshots.md)


## What hardware do you use?:

<details><summary>Around the house I have:</summary>
<p>

 - A Dell Wyse thin client with 128GB SSD-Dom, with a CSL bluetooth adapter.  This is the main hub of my Home Automation system, and also has a 1TB external harddrive which functions as a NAS.

 - 3 x - NodeMCU boards with PIR sensors

 - A Raspberry pi based RF transmitter/receiver

 - VM wifi router - connecting everything together.

 - Netgear 5 port switch - allowing to have lots of wired connections for reliability.

 - Philips Hue Bridge

 - 3 x Hue Colour bulbs.

 - 9 x Hue White bulbs.

 - Hue Tap (Scene controller).

 - 3 x Hue dimmer (light controller).

 - 5 x Hue motion sensor.

 - A Broadlink RM3 IR sender - to control non-smart infra-red devices.

 - A Wetek Openelec - running Kodi.

 - 5 x Google Chromecast Audios - for multi-room music.

 - Usual home theatre stuff - TV/Blu-Ray/AV Receiver/Games Consoles

 - 2 x Amazon Echo Dots - for voice control.

 - Telegram App (on mobiles) - for two-way conversations with Homeassistant.

</p>
</details>


<details><summary>This might help to visualise what's going on with my hardware devices:</summary>
<p>

I live in a 3 storey townhouse, consisting of:
 - A living area on the ground floor (Living room and kitchen/diner)
 - Hall stairs and landing leading to first floor.
 - Boys' bedroom, Girls' bedroom and bathroom on the first floor.
 - Stairs leading to Master bedroom on the second floor.

</p>
</details>


## Where can I find out more about this stuff?

Have a look at the [Wiki](https://github.com/mf-social/Home-Assistant/wiki) to see how I've put it all together.

<details><summary>Some really useful resources are:</summary>
<p>

[Home Assistant](http://home-assistant.io) and the [Community Forum](https://community.home-assistant.io/)

[Bruh's website](http://www.bruhautomation.com/) and [Youtube](https://www.youtube.com/c/bruhautomation1)

[HA examples](https://home-assistant.io/cookbook/) especially [CCOSTAN](https://github.com/CCOSTAN/Home-AssistantConfig)

[CircleCI](https://circleci.com) for checking configuration.

[Uptime Robot](https://uptimerobot.com/) for checking my system is online.

[Dropbox](https://www.dropbox.com/) and [Martikainen87's sync script](https://github.com/martikainen87/Home-Automation/wiki/Backup-your-configuration-to-Dropbox) for managing backups.
</p>
</details>
