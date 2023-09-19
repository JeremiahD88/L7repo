#!/usr/bin/python3

import gpiozero

button = gpiozero.Button(20)
while (1):
	if button.is_pressed:
		print('Button is pressed')
		break




