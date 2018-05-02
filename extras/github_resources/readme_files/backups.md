# Keeping everything running smoothly

## Checking my Homeassistant is online

One thing you cannot monitor from within homeassistant itself is if it crashes, or for some other reason goes 'offline'.  This is because if it is offline it cannot send you a message to tell you about it!  To make sure I am kept up-to-date if there is a problem I use [Uptime Robot](https://uptimerobot.com/) .  This service simply checks to see if my web front end is reachable every few minutes, and sends me a message on Telegram if it cannot get through.

## How I manage backups

I upload all my non-sensitive files to GitHub, which means I have a backup of them, but also I can check my config online for most things.  I can edit the files locally or edit the config on GitHub and then make my HA instance pull the updates so I can remotely reconfigure the machine if needed.  Guide to how I'm doing this coming soon.

The Master Branch of my repo is protected, so I cannot push updates to it and must merge code in a PR.  I use TravisCI to check my config every time a PR is created this runs a program that checks the configuration is sound.  If the configuration check fails I cannot merge the PR.  Because this requires a `secrets.yaml` file I have added a fake version of this in the extras/github_resources folder.  My `.travis.yml` script then moves this file to the correct place before running the program to prevent false negatives.  The redacted version of `secrets.yaml` is identical in format and layout to my real `secrets.yaml` so you can see how it is organised.

In addition to backing up my config here, I also backup my entire /.homeassistant/ directory (including all my configuration files and secrets.yaml etc) to dropbox using the method described [here](https://github.com/martikainen87/Home-Automation/wiki/Backup-your-configuration-to-Dropbox) .  This means that should I have a total system failure, I can simply reinstall debian, reinstall Homeassistant, and drop my full working configuration back in.  My script uses rsync to copy all of the contents of the directoy except the log and database to a backup folder (this prevents me uploading gigabytes of database entries to dropbox that I would not need in the event of a reinstall), and then uses the dropbox_sync script to upload that to dropbox.
