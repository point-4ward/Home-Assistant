# My Home Assistant setup:

This is my current Home Automation setup.  Starting small and gradually growing as funds allow...

## House:

3 storey townhouse, laid out (basically) like...

```
            **Front**            **Back**

2nd floor - Master bedroom     Master bedroom
          - Master bedroom     Master bedroom

1st floor - Boys room          Bathroom
          - Boys room          Girls room

Gnd floor - Living room        Kitchen
          - Living room        Kitchen
```

Click here to see the [Hardware and Software](extras/readme_files/hardware_software.md) I am using.

## What it does:

 - Controllable from our phones over the internet, or via local network.
 - Controls living room lights, bedroom lights and landing light.  The master bedroom lights are multicoloured and can be set to preset scenes or controlled individually.  The living room lights are white but can be set to preset brightness or controlled to any desired level.
 - Tracks our phones using owntracks and therefore knows whether or not anybody is at home.
 - Notifies us of key events via telegram and/or notifications on screen via kodi.
 - Reacts to incoming messages sent from telegram.
 - Master bedroom lights can also be controlled by Hue Tap which has 4 buttons (3 pre-programmed scenes and off).
 - Living room lights can also be controlled with Hue Dimmer.
 - Automatically pause media during phone call using Yatse.
 - Automatically turn living room lights on when it gets dark and somebody is home.
 - Automatically turn living room lights on if the house is empty and somebody arrives home in the dark.
 - Automatically set living room lights to 'dim' when playing media (except music) and it is dark.
 - Automatically set living room lights to 'normal' when media (except music) pauses or stops.
 - Landing light comes on following the same rules as the living room light, but then dims to a night-light at 21.30 hours and switches off at sunrise.
 - Voice control for all the lights.
 - Voice control Kodi.
 - Voice output via Chromecast Audios.
 - Multiroom audio with streaming radio stations.
 - Monitors email addresses for security breaches and notifies if insecure.
 - Monitors HomeAssistant for updates and notifies when update available.
 - Monitors HomeAssistant for restarts and alerts me if I was not doing maintenance, in case of power cuts.
 - Automatically updates Let's Encrypt certificate for SSL.
 - Monitors the instance for hacking attempts, notifies and blocks IP of attacker.
 - Alarm clock function that switches on lights and sends an audio alert through Chromecast Audios.
 - Timer function that alerts on phones and over Chromecast Audios.
 - Sets a UI theme based on time of day.
 
## Configuration

Click here to see [how I've configured it](extras/readme_files/configuration.md) and how this repo is organised.

Click here to see how I [manage backups and ensure my config is valid](extras/readme_files/backups.md) with GitHub, TravisCI and Dropbox.

## Useful links/resources etc:

[Home Assistant](http://home-assistant.io) | [Owntracks](http://owntracks.org/) | [Yatse](http://yatse.tv/redmine/projects/yatse)

[Bruh's website](http://www.bruhautomation.com/) and [Youtube](https://www.youtube.com/c/bruhautomation1)

[HA examples](https://home-assistant.io/cookbook/) espescially [CCOSTAN](https://github.com/CCOSTAN/Home-AssistantConfig) and [Bruh](https://github.com/bruhautomation/BRUH3-Home-Assistant-Configuration)

## Information

[![TravisCI](https://travis-ci.org/mf-social/Home-Assistant.svg?branch=master)](https://travis-ci.org/mf-social/Home-Assistant) <---This shows whether the configuration in this repo is valid. [Version I'm running.](.HA_VERSION)

[![GitHub issues](https://img.shields.io/github/issues/mf-social/Home-Assistant.svg)](https://github.com/mf-social/Home-Assistant/issues) <--- This is like my TODO list

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-blue.svg?style=flat)](https://github.com/mf-social/Home-Assistant/pulls) <--- If you have any ideas, they're always welcome.  Either submit an issue or a PR, or drop me a message!