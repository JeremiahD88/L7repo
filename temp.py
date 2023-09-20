#!/usr/bin/python3

f = open('/sys/bus/w1/devices/28-062018a55525/temperature', mode = 'r')

temp = float(f.readline())

f.close()
print(f'The temperature is: {temp/1000}')
