# paoloserver

Stick launch.sh into the launch script box when you start your Lightsail instance

Rebooting the instance won't rerun the launch script, so if you change stuff and pushed a new image to Docker Hub you have to either make a new instance and (probably???) reconfigure DNS, or just ssh in and docker pull and docker run again.
