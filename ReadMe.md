BeetBox
=======

This is probably not especially useful to anyone, but may be interesting to those curious about the inner workings of the [Beetbox](http://scott.j38.net/interactive/beetbox/).

The code for interfacing with the MPR121 is based on [an Arduino example by Jim Lindblom](http://bildr.org/2011/05/mpr121_arduino/).

Fixes by hlessil
================

- Fixed bug where pins 8-11 were inaccessible due to reading of only one byte instead of a word.
- Added script that should be added to /etc/init.d to make beetbox a linux daemon (start on boot) based on instructions found here: http://blog.scphillips.com/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
- Changed sound files to numbers, made them absolute paths in the code as a quick dirty hack for daemon.

TIPS
====

- you can test sound files with the aplay command (e.g 'aplay samples/kick.wav')
- run sudo raspi-config and under Advanced Options force audio to 3.5mm
- use alsamixer to set up volume via the command line
- set up a link local address (e.g. 169.254.3.14) so that you can talk to your rpi via an ethernet cable to your workstation
- check this out for enabling i2c: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
- if the raspi doesn't see the MPR121 chip, check your wiring and soldering connections
