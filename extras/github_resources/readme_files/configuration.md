# My configuration:

See in the repo for all of my non-sensitive configuration files.  I've been playing with HA for a while now and have made a fair few changes, and have now decided to organise my files in a package-based system.

I have put a comment block at the top of each file that hopefully will explain what each one is for, for anyone using this repo as a learning tool, or for anyone that wants to copy any of the packages.

It essentially works like this:

All your homeassistant files are contained within your `/path/to/.homeassistant/` directory.  Inside this directory are some files that can't be moved such as `secrets.yaml` , `known_devices.yaml` and (most importantly) `configuration.yaml` .

There are various ways to split the configuration.yaml in to smaller chunks with !include statements, this is detailed here **TODO - link to splitting configuration**

I've chosen to split the configuration in to packages (detailed here **TODO - link to packages docs**), and create devices or utilities by grouping components and sensors together.  These are placed in a folder called `config/` .

I then have an `extras/` folder that contains my bash scripts and github resources (including a redacted version of my `secrets.yaml` ).  I also have a `private/` folder that contains things relevant to my installation but I don't want to uplad to github as they contain sensitive information and sanitised versions will be of no use to anyone.

The end result looks like this:

```
.homeassistant/
    |
    |- configuration.yaml
    |- secrets.yaml
    |- travis.yml
    |- [other unmoveable configuration files and directories]
    |
    |-----/private/
    |      |
    |      |- [useful things that don't beling on github]
    |
    |-----/config/
    |      |
    |      |-----/packages/
    |      |      |
    |      |      |-----/devices/
    |      |      |      |        
    |      |      |      |-[file per packaged device]
    |      |      |
    |      |      |-----/utilities/
    |      |             |
    |      |             |-[file per packaged utility]
    |      |
    |      |-----/automation/
    |      |      |
    |      |      |-[files for each automation, separated by room/group directories]
    |      |
    |      |-----/scene/
    |      |      |
    |      |      |-[files for each scene, separated by room/group directories]
    |      |
    |      |-----/script/
    |      |      |
    |             |-[files for each script, separated by room/group directories]
    |
    |
    |-----/extras/
           |
	   |-----/bash_scripts/
	   |      |
	   |      |-[useful scripts that can be called from homeassistant]
	   |
	   |-----/github_resources/
	          |
		  |- secrets_redacted.yaml
		  |
		  |-[readme files, screenshots and guides]
```

