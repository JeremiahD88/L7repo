#!/usr/bin/python3

import sys
import time
import gpiozero


on_time = float((sys.argv[1]))
off_time = float((sys.argv[2]))
blink_time = int((sys.argv[3]))


my_led = gpiozero.LED(24)


#for i in range (0,blink_time):
#	my_led.on()
#	time.sleep(on_time)
#	my_led.off()
#	time.sleep(off_time)
my_led.blink(on_time,off_time,blink_time)


