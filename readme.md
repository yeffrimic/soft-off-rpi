# soft-off-rpi

This is a way to shutdown the raspberry pi using an attiny 85 to convert the voltage from a sensor or a battery and a python scritp that allows to take actions like shutdown the raspberry or kill processes 

## Serial to analog Converter firmware

this is just an analog read from attiny and send it through Serial (software) to de Raspberry pi pin RX(pin number 10 in gpio) sending data from 0 to 1023 that is equals 0 to 5 volts. 

## soft-off-digital.py 

this is the python software that receives the data from the attiny with the S0 port or the serial gpio port from the raspberry and convert it again to 0 to 5 volts and make choices of what to do. 

## soft-off-digital.sh 

This is a bash script that makes init the soft-off-digital.py from boot start and stop killing the process. 

Read the install.md