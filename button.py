#!/usr/bin/python3

import gpiozero
import signal

button = gpiozero.Button(20)

def say_hello():
	print('Hello')

button.when_pressed = say_hello


while(1):
	my_input = int(input('Bla'))	
	print('Hejeh')



