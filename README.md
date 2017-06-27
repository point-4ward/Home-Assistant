[![TravisCI](https://travis-ci.org/mf-social/Home-Assistant.svg?branch=master)](https://travis-ci.org/mf-social/Home-Assistant) [![RepoSize](https://reposs.herokuapp.com/?path=mf-social/Home-Assistant)](https://github.com/ruddfawcett/reposs) [![GitHub issues](https://img.shields.io/github/issues/mf-social/Home-Assistant.svg)](https://github.com/mf-social/Home-Assistant/issues)

# My HA setup:

This is my current Home Automation setup.  Starting small and gradually growing as funds allow...

## House:

3 storey townhouse, laid out (basically) like...

```
            **Back**               **Front**

2nd floor - En Suite           Master bedroom
          - Master bedroom     Master bedroom

1st floor - Family bathroom    Bedroom 4
          - Bedroom 2          Bedroom 3

Gnd floor - Living room        WC
          - Living room        Kitchen
```

## Hardware:

 - Raspberry Pi 3
 - Z-wave.me Razberry module
 - Wetek Openelec (Kodi)
 - Amazon Echo Dot
 - Asus wifi router with USB NAS attached
 - Philips Hue Bridge
 - Philips Hue Tap
 - 3 x Philips Hue colour bulbs (master bedroom)
 - 2 x Fibaro FGD-212 dimmers (living room and bedroom2)
 - Fibaro FGMS-001 multi-sensor (yet to be fitted)
 - Comag 10" tablet
 - Usual home theatre stuff - TV/Blu-Ray/AV Receiver
 - 3 x Chromecast Audios

## Software:

 - Home Assistant
 - Kodi
 - Yatse (+ call plugin)
 - Alexa app (for config of echo dot)
 - Hue app (for config of hue lights/bridge)
 - Custom Alexa skill (to control Kodi via Echo Dot)
 - Google Home app (for config of Chromecasts)
 - Owntracks
 - Telegram - two way conversations with Home Assistant

## What it does:

 - Controllable from my phone over the internet, or via local network.
 - Controls living room lights, bedroom 2 lights and three lights in the master bedroom ( 1 x ceiling, 2 x bedside).  The master bedroom lights are multicoloured and can be set to preset scenes or controlled individually.  The living room and bedroom 2 lights are white but can be set to preset brightness or controlled to any desired level.
 - Tracks our phones using owntracks and therefore knows whether or not anybody is at home.
 - Notifies us of key events via telegram and/or notifications on screen via kodi.
 - Reacts to incoming messages sent from telegram.
 - Master bedroom lights can also be controlled by Hue Tap which has 4 buttons (3 pre-programmed scenes and off).
 - Automatically pause media during phone call using Yatse.
 - Automatically turn living room lights on when it gets dark and somebody is home.
 - Automatically turn living room lights on if the house is empty and somebody arrives home in the dark.
 - Automatically set living room lights to 'dim' when playing media (except music) and it is dark.
 - Automatically set living room lights to 'normal' when media (except music) pauses or stops.
 - Living room lights will come on in the day if heavily overcast outside, and will switch off again when clouds pass.
 - Voice control for all the lights.
 - Voice control Kodi.
 - Voice output via Chromecast Audios.
 - Multiroom audio with streaming radio stations.
 - Monitors email addresses for security breaches and notifies if insecure.
 - Monitors HomeAssistant for updates and notifies when update available.
 - Automatically updates Let's Encrypt certificate for SSL.
 - Monitors the instance for hacking attempts, notifies and blocks IP of attacker.
 - Alarm clock function that switches on lights and sends an audio alert through Chromecast Audios.
 - Timer function that alerts on phones and over Chromecast Audios. 

## My configuration:

See in the repo for all of my non-sensitive configuration files.  I've been playing with HA for a while now and have made a fair few changes, a few quick notes:

In my configuration.yaml I have removed history component, discovery component and conversation component. Most people seem to leave these in but I removed them because:

 - The history component paints lovely pretty bars of the state that your components have been in recently.  I didn't need this, and found that it was quite slow to render, so it's gone.  I find the logbook a far more useful tool anyway.
 - The discovery component never discovered anything for me, so having it running in the background seemed a waste of resources.
 - The conversation component is superfluous with my amazon echo implementation, so again I've reclaimed some resources.
 
I have changed my logging database to mysql.  I read on a blog post once that it massively improves the speed of HA.  In all honesty I did not notice such a change to the performance of HA, but I've done it now so I'm not changing it back unless I have a specific reason to. 

Everybody has their own way of organising files, and they can get confusing, so I decided on an organisational method for mine from the start and this is how I work it:

In the '.homeassistant/' folder there are some files that can't be moved, so they obviously stay there.  Any that don't have to be there (and don't have to be in a specific location elswewhere, ie local icons in ./homeassistant/www/) go in a folder called config/

When I'm adding an entry to my configuration.yaml I ask myself whether it will take more than three lines.  If it takes only one, two or three lines, I put it directly in configuration.yaml

Example:
```
#####Fine:

sun:        <---------  One line

media_player:
  - platform: kodi
    host: 192.168.0.123  <----- Three lines

#####Not fine
mqtt:
  broker: !secret mqtt_broker
  port: !secret mqtt_port
  client_id: !secret mqtt_client_id <---- Four lines or more
  keepalive: 60
  username: !secret mqtt_username
  password: !secret mqtt_password
```

	
	
Where the entry will take four lines or more, I use an include and place the include file in the config/misc/ directory.  I use the exact name of the component for the include, eg:
```
mqtt: !include config/misc/mqtt.yaml
```

In cases where the new include file becomes large (I favour keeping them in bite-sized chunks of around 50 lines or fewer), I split that file in to as many as are needed and place them in a folder named exactly after the component, eg:
```
zone: !include_dir_list config/zone/
```

You may note that by following this rule I have also, contrary to convention, done this with my 'homeassistant:' core instance, placing the multiple-lined entries in an included file located at /config/core/homeassistant.yaml  .  (I put it in the folder 'core' to keep it separate from the non-core components.)

I have also used 'packages' to group some items together in to a combined 'device' (like a radio player for my chromecasts, and an alarm clock function that switches on lights), the configuration files for which are also kept in bite-sized chunks using the above method, although the includes are nested slightly to prevent duplicates from recursively merged folders.

This means I can keep all the configuration files in an order that makes sense to me, and keeps them small so they are easy to debug.  The only files in my system with more than 50 lines are `configuration.yaml` and `secrets.yaml` .

All of which, for me, leads to an easy to manage configuration system that looks something like this...

```
/path/to/.homeassistant/
        |
        |- configuration.yaml
        |- google_calendars.yaml
        |- known_devices.yaml
        |- secrets.yaml
        |...[log files etc]
        |
        |-----/www/
        |     |
        |     |...[local pictures and files here]
        |
        |-----/deps/
        |     |
        |     |...[dependencies]
        |
        |-----/extras/
        |     |
        |     |...[bash scripts/github resources etc]
        |
        |-----/config/
              |
              |-----/automation/
              |     |
              |     |...[Folder per room/group]
              |           |
              |           |...[File per automation]
              |
              |-----/camera/
              |     |
              |     |...[Folder per type]
              |           |
              |           |...[File per camera]		
              |
              |-----/core/
              |     |
              |     |- customize_glob.yaml
              |     |- homeassistant.yaml
              |     |- packages.yaml
              |     |
              |     |-----/customize/
              |     |     |
              |     |     |...[File per group/set]
              |     |
              |     |-----/packages/
              |           |
              |           |...[File per package]
              |           |		
              |           |...[Folder per package for elements]
              |                 |
              |                 |...[File per package element]
              |
              |-----/group/
              |     |
              |     |-----/cards/
              |     |     |
              |     |     |...[file for each UI card]
              |     |
              |     |-----/views/
              |           |
              |           |...[file for each UI view tab]
              |
              |-----/misc/
              |     |
              |     |- alarm_control_panel.yaml
              |     |- android_ip_webcam.yaml
              |     |- binary_sensor.yaml
              |     |- device_sun_light_trigger.yaml
              |     |- device_tracker.yaml
              |     |- emulated_hue.yaml
              |     |- http.yaml
              |     |- input_boolean.yaml
              |     |- input_select.yaml
              |     |- logbook.yaml
              |     |- media_player.yaml
              |     |- mqtt.yaml
              |     |- notify.yaml
              |     |- shell_command.yaml
              |     |- telegram_bot.yaml
              |     |- weblink.yaml
              |
              |-----/scene/
              |     |
              |     |...[folder for each room/group]
              |           |
              |           |...[File per scene]
              |
              |-----/script/
              |     |
              |     |...[folder for each room/group]
              |           |
              |           |...[File per script]		
              |
              |-----/sensor/
              |     |
              |     |...[file for each group/set]
              |
              |-----/zone/
                    |
                    |...[file for each zone]
	
```				

...which you can browse through in this repo.

I have put a small comment block at the top of each file that hopefully will give some clues for anyone using this repo as a learning tool.  At some point in the future I will try and put some more detailed comments on the more important/complicated bits.  In the meantime, if I can clarify anything for anyone, just let me know.

I use TravisCI to check my config every time it is pushed to Github.  This runs a program that checks the configuration is sound and alerts me if it is not.  Because this requires a `secrets.yaml` file and an `SSL certificate` I have added fake versions of these in the extras/travis_ci folder.  My `.travis.yml` script then moves these files to the correct place before running the program to prevent false negatives.  The redacted version of `secrets.yaml` is identical in format and layout to my real `secrets.yaml` so you can see how it is organised.

## Useful links/resources etc:

[Home Assistant](http://home-assistant.io)

[Owntracks](http://owntracks.org/)

[Yatse](http://yatse.tv/redmine/projects/yatse)

[HAdashboard](http://home-assistant.io/docs/ecosystem/hadashboard/dash_config/)

[Bruh's website](http://www.bruhautomation.com/) and [Youtube](https://www.youtube.com/c/bruhautomation1)

[HA examples](https://home-assistant.io/cookbook/) espescially [CCOSTAN](https://github.com/CCOSTAN/Home-AssistantConfig) and [Bruh](https://github.com/bruhautomation/BRUH3-Home-Assistant-Configuration)


## Things to do:

Put some images on here

Timeline of automations / conditions to trigger

Buy more stuff!