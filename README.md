TalkBox
=======

This project is a fork of the [Beetbox](http://scott.j38.net/interactive/beetbox/) project by ScottGarner and his port of the MPR121 library based on [an Arduino example by Jim Lindblom](http://bildr.org/2011/05/mpr121_arduino/).

The idea is to make a modular and easy-to-assemble device to enable students with cognitive, physical or developmental disabilities. Eventually, it could be used for anything from a communication aid, a teaching aid, to being a project on its own for assembly by students.

Hardware
========
- [MPR121 Capacitive Touch Sensor Breakout Board](https://www.sparkfun.com/products/9695)
- [RaspberryPi](http://www.raspberrypi.org/)
- some headers and wires


Instructions
============

To be updated as the project takes shape:

- Download the TalkBox image.
- dd image onto SD card.
- Plug MPR121 board into GPIO
- Plug into electricity and use
- For modifications modify JSON, use GUI, or web interface (will pick and develop one for now).


Version Updates
===============

v0.2:
- Fixed bug where pins 8-11 were inaccessible due to reading of only one byte instead of a word.
- Added script that should be added to /etc/init.d to make TalkBox a linux daemon (start on boot) based on instructions found here: http://blog.scphillips.com/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
- Changed sound files to numbers, made them absolute paths in the code as a quick dirty hack for daemon.

TIPS
====

- you can test sound files with the aplay command (e.g 'aplay samples/kick.wav')
- run sudo raspi-config and under Advanced Options force audio to 3.5mm
- use alsamixer to set up volume via the command line
- set up a link local address (e.g. 169.254.3.14) so that you can talk to your rpi via an ethernet cable to your workstation
- check this out for enabling i2c: http://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
- if the raspi doesn't see the MPR121 chip, check your wiring and soldering connections
