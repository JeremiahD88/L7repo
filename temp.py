#!/usr/bin/python3
import sys
import time

file_path = str(sys.argv[1])
num_data = int(sys.argv[2])
file_w = open(file_path, mode = 'w')

for i in range(0,num_data):
    
    file_r = open('/sys/bus/w1/devices/28-062018a55525/temperature', mode = 'r')
    data = int(file_r.readline())
    file_r.close()
    #file_w.write('\n')
    file_w.write(str(data / 1000))
    file_w.write('\n')
    time.sleep(1)
file_w.close()