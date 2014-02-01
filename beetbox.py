#!/usr/bin/env python

"""beetbox.py: Trigger script for the BeetBox."""

__author__ = "Scott Garner"
__email__ = "scott@j38.net"

import pygame

import RPi.GPIO as GPIO
import mpr121

# Use GPIO Interrupt Pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)

# Use mpr121 class for everything else

mpr121.TOU_THRESH = 0x30
mpr121.REL_THRESH = 0x33
mpr121.setup(0x5a)

# User pygame for sounds

pygame.mixer.pre_init(44100, -16, 12, 512)
pygame.init()

sounds = []

sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/0.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/1.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/2.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/3.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/4.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/5.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/6.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/7.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/8.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/9.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/10.wav'))
sounds.append(pygame.mixer.Sound('/home/pi/devt/BeetBox/samples/11.wav'))

for sound in sounds:
	sound.set_volume(.65)

# Track touches

touches = [0,0,0,0,0,0,0,0,0,0,0,0];

while True:

	if (GPIO.input(7)): # Interupt pin is high
		pass
	else: # Interupt pin is low

		touchData = mpr121.readWordData(0x5a)

		for i in range(12):
			if (touchData & (1<<i)):

				if (touches[i] == 0):

					print( 'Pin ' + str(i) + ' was just touched')

					sounds[i].play()

				touches[i] = 1;
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				touches[i] = 0;
