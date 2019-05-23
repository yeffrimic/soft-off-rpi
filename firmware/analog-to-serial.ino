/*
 * Analog to serial converter
 * this is a sketch that receives analog data from 
 * the analog pin and send it through serial just one way 
 * 
 * Yeffri J. Salazar
 * Xibalba hackerspace, mayo 2019 
 *
 */


#include <SoftwareSerial.h>
#define outputSerialPin 3 
SoftwareSerial output(4, outputSerialPin);


void setup() {
  output.begin(9600);
}

void loop() {
  int batteryValue = analogRead(A1); // get the analog reading and get values from 0 to 1023 
  output.print(String(batteryValue) + "\r\n");

}
