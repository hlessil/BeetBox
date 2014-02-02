#!/usr/bin/env python

"""talkbox.py: Trigger script for the TalkBox."""

import os
import json
import pygame

import RPi.GPIO as GPIO
import mpr121

# Simplest to manage as globals in such a small script
sound_index = 0
volume_level = .60

def get_soundsets(soundset_dir):
	"Get relevant soundsets configurations contained in soundset_dir path."
	soundsets = []
	CONF_JSON = 'soundconf.json'
	soundset_dirs = ['/home/pi/TalkBox/sounds']

	for root, dirs, files in os.walk(soundset_dir):
		if CONF_JSON in files and not 'example' in root:
			soundconf = json.load(open(root + os.sep + CONF_JSON, 'r'))
			soundconf['rootdir'] = root
			soundsets.append(soundconf)
	return soundsets


def next_soundset():
	global sound_index
	sound_index = (sound_index + 1) % len(soundsets)
	sounds = extract_sound(soundsets[sound_index])
        soundset_filename = soundsets[sound_index]['rootdir'] + os.sep + soundsets[sound_index]['soundset_filename']
        create_sound(soundset_filename).play()
	return sounds

def prev_soundset():
	global sound_index
	sound_index = (sound_index - 1) % len(soundsets)
        sounds = extract_sound(soundsets[sound_index])
	soundset_filename = soundsets[sound_index]['rootdir'] + os.sep + soundsets[sound_index]['soundset_filename']
	create_sound(soundset_filename).play()
	return sounds

def extract_sound(soundset):
	sounds = {}
	for key, value in soundset['sounds'].iteritems():
		sound = create_sound(soundset['rootdir'] + os.sep + value['filename'])
	        sounds[int(key)] = sound
	return sounds

def inc_volume(sounds):
	global volume_level
	volume_level = min(1.0, volume_level + 0.1)
	for sound in sounds.values():
		sound.set_volume(volume_level)
	pop_sound.set_volume(volume_level)
	pop_sound.play()
	return sounds

def dec_volume(sounds):
	global volume_level
	volume_level = max(0.0, volume_level - 0.1)
	for sound in sounds.values():
                sound.set_volume(volume_level)
	pop_sound.set_volume(volume_level)
        pop_sound.play()
	return sounds

def create_sound(sound_path):
	sound = pygame.mixer.Sound(sound_path)
	sound.set_volume(volume_level)
	return sound

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


pop_sound = create_sound('sounds/pop.wav')
soundsets = get_soundsets('/home/pi/TalkBox/sounds')
# TODO soundsets = soundsets + get_soundsets('/path/to/USB/mount')
sounds = next_soundset()


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

					if (i < 8):
						sounds[i].play()
					elif (i == 8):
						sounds = prev_soundset()
					elif (i == 9):
						sounds = next_soundset()
					elif (i == 10):
						sounds = dec_volume(sounds)
					elif (i == 11):
						sounds = inc_volume(sounds)

				touches[i] = 1;
			else:
				if (touches[i] == 1):
					print( 'Pin ' + str(i) + ' was just released')
				touches[i] = 0;
