# How I manage backups

I upload all my non-sensitive files to GitHub, which means I have a backup of them, but also I can check my config online for most things.  I can edit the files locally or edit the config on GitHub and then make my HA instance pull the updates so I can remotely reconfigure the machine if needed.  Guide to how I'm doing this coming soon.

I use TravisCI to check my config every time it is pushed to Github.  This runs a program that checks the configuration is sound and alerts me if it is not.  Because this requires a `secrets.yaml` file I have added a fake version of this in the extras/github_resources folder.  My `.travis.yml` script then moves this file to the correct place before running the program to prevent false negatives.  The redacted version of `secrets.yaml` is identical in format and layout to my real `secrets.yaml` so you can see how it is organised.

In addition to backing up my config here, I also backup my entire /.homeassistant/ directory (including all my configuration files and secrets.yaml etc) to dropbox using the method described [here](https://github.com/martikainen87/Home-Automation/wiki/Backup-your-configuration-to-Dropbox) .  This means that should I have a total system failure, I can simply reinstall raspian, reinstall homeassistant, and drop my full working configuration back in.
