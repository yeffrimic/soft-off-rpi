"""
Soft-off-digital.py 

This software receives data from serial port on /dev/ttyS0
activated in Raspberry pi. 
The data comes from the attiny 85 with analog to serial converter 
firmware. 
This firmware sends the voltage data in format of 4 bytes
from 0 to 1023. 

Yeffri J. Salazar
Xibalba Hackerspace, may 2019 

"""
#!/usr/bin/env python3
import serial
import subprocess
a = 5/1024 # this is the float number per unit from 0 to 1023 

battery_alert_voltage = 3.2
#Open the serial port in Raspberry pi the S0 in GPIO 

ser = serial.Serial(
        port='/dev/ttyS0',
        baudrate = 9600
)

while (ser.is_open==False):
    ser.open()


while True:
    ser_bytes = ser.readline()
    decoded_bytes = ser_bytes.decode("utf-8")
    if(len(decoded_bytes) >=3):#we have to check the data if we have some read error 
        battery_voltage =  int(decoded_bytes) * a
        if(battery_voltage <= battery_alert_voltage):#if the battery is low we turn off the rpi or kill the process
            print("shutting off")
            subprocess.call(['shutdown', '-h', 'now'], shell=False)
    else:
        pass

