# My configuration:

See in the repo for all of my non-sensitive configuration files.  I've been playing with HA for a while now and have made a fair few changes, a few quick notes:

In my configuration.yaml I have removed history component, discovery component and conversation component. Most people seem to leave these in but I removed them because:

 - The history component paints lovely pretty bars of the state that your components have been in recently.  I didn't need this, and found that it was quite slow to render, so it's gone.  I find the logbook a far more useful tool anyway.
 - The discovery component never discovered anything for me, so having it running in the background seemed a waste of resources.
 - The conversation component is superfluous with my amazon echo implementation, so again I've reclaimed some resources.

Everybody has their own way of organising files, and they can get confusing, so I decided on an organisational method for mine from the start and this is how I work it:

In the '.homeassistant/' folder there are some files that can't be moved, so they obviously stay there.  Any that don't have to be there (and don't have to be in a specific location elswewhere, ie local icons in ./homeassistant/www/) go in a folder called config/

When I'm adding an entry to my configuration.yaml I ask myself whether it will take more than three lines.  If it takes only one, two or three lines, I put it directly in configuration.yaml file.  I have split this file in to four sections: 'core', 'interface', 'components' and 'automations/scripts/etc'.

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

	
	
Where the entry will take four lines or more, I use an include and place the include file in the config/ directory, in the subdirectory based on whether it is a 'core' element, an 'interface' element or whatever.  I use the exact name of the component for the include, eg:
```
mqtt: !include config/components/mqtt.yaml
```

In cases where the new include file becomes large (I favour keeping them in bite-sized chunks of around 50 lines or fewer), I split that file in to as many as are needed and place them in a folder named exactly after the component, eg:
```
zone: !include_dir_list config/components/zone/
```

I have also used 'packages' in the core configuration to group some items together in to a combined 'device' (like a radio player for my chromecasts, and an alarm clock function that switches on lights and plays music), as these create a single device I have kept that configuration together.

This means I can keep all the configuration files in an order that makes sense to me, and keeps them small so they are easy to debug.  The only files in my system with more than 50 lines are `configuration.yaml` , `secrets.yaml` and the packages.  I then use a folder called 'extras' to hold anything else relevent to the install or to enhance this repo(like bash scripts and github resources).

All of which, for me, leads to an easy to manage configuration system that looks something like this...

```
/path/to/.homeassistant/
        |
        |- configuration.yaml
        |- google_calendars.yaml
        |- ip_bans.yaml
        |- known_devices.yaml
        |- secrets.yaml
        |...[log files etc]
        |
        |-----/www/
        |     |
        |     |...[local pictures and files here]
        |
        |-----/extras/
        |     |
        |     |...[bash scripts/github resources etc]
        |
        |-----/config/
              |
              |-----/components/
              |     |
              |     |- emulated_hue.yaml
              |     |- media_player.yaml
              |     |- mqtt.yaml
              |     |- notify.yaml
              |     |- telegram_bot.yaml
              |     |- weblink.yaml
              |     |
              |     |-----/camera/
              |     |     |
              |     |     |...[Folder per type]
              |     |          |
              |     |          |..[File per camera]
              |     |
              |     |-----/sensor/
              |     |      |
              |     |      |...[File for each group/set]
              |     |
              |     |-----/zone/
              |            |			  
              |            |...[File for each zone]
              |
              |-----/core/
              |     |
              |     |- customize_glob.yaml
              |     |- homeassistant.yaml
              |     |
              |     |-----/customize/
              |     |     |
              |     |     |...[File per group/set]
              |     |
              |     |-----/packages/
              |           |
              |           |...[File per package]
              |			  
              |-----/etc/
              |     |
              |     |- input_boolean.yaml
              |     |- input_select.yaml
              |     |- shell_command.yaml
              |     |
              |     |-----/automation/
              |     |     |
              |     |     |...[Folder per room/group]
              |     |          |
              |     |          |...[File per automation]
              |     |
              |     |-----/scene/
              |     |     |
              |     |     |...[Folder per each room/group]
              |     |          |		
              |     |          |...[File per scene]
              |     |
              |     |-----/script/
              |           |
              |           |...[Folder per each room/group]
              |                |		
              |                |...[File per scene]
              |
              |-----/interface/
                    |
                    |- http.yaml
                    |- logbook.yaml
                    |
                    |-----/group/
                    |     |
                    |     |-----/cards/
                    |     |     |
                    |     |     |...[File for each UI card]
                    |     |
                    |     |-----/views/
                    |           |
                    |           |...[File for each UI view tab]
                    |
                    |-----/themes/
                          |
                          |...[File per theme]						  
```				

...which you can browse through in this repo.

I have put a small comment block at the top of each file that hopefully will give some clues for anyone using this repo as a learning tool.  At some point in the future I will try and put some more detailed comments on the more important/complicated bits.  In the meantime, if I can clarify anything for anyone, just let me know.