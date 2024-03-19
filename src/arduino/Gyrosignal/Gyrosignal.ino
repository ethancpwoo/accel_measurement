#include <Wire.h>
#define accel_module (0x53)

// define global variables
byte values[6]; //return values
char output[512]; //output string
int data_register = 0x32;
int x, y, z;
float accel_x, accel_y, accel_z, mag;

void setup() {
  Wire.begin();
  Serial.begin(9000);

  // Write to power ctrl 0 to clear register
  Wire.beginTransmission(accel_module); 
  Wire.write(0x2D);
  Wire.write(0);
  Wire.endTransmission();

  // Write to power ctrl bit to begin measure mode
  Wire.beginTransmission(accel_module); 
  Wire.write(0x2D);
  Wire.write(16);
  Wire.endTransmission();

  // Write to power ctrl bit to disable sleep mode
  Wire.beginTransmission(accel_module); 
  Wire.write(0x2D);
  Wire.write(8);
  Wire.endTransmission();

}

void loop() {

  // Read from data register
  Wire.beginTransmission(accel_module);
  Wire.write(data_register);
  Wire.endTransmission();

  // From next 6 bits, request the data
  Wire.beginTransmission(accel_module);
  Wire.requestFrom(accel_module, 6);

  //Go bit by bit and append into values
  int index = 0;
  while(Wire.available())
  {
    values[index] = Wire.read();
    index++;
  }
  Wire.endTransmission();

  // bitwise operations to convert 6 bytes into coherent values
  // value[1] has MS byte in twos complement and value[0] has LS byte in twos complement
  // since value[i] is a byte, shift left 8 bits and or the previous byte
  x = (((int)values[1] << 8) | values[0]);
  y = (((int)values[3] << 8) | values[2]);
  z = (((int)values[5] << 8) | values[4]);

  accel_x = x * 0.039;
  accel_y = y * 0.039;
  accel_z = z * 0.039;

  mag = sqrt(sq(accel_x) + sq(accel_y) + sq(accel_z));
  Serial.println(mag);
  
  // Serial.print(accel_x);
  // Serial.print(' ');
  // Serial.println(accel_y);
  // Serial.print(' ');
  // Serial.println(accel_z);

  delay(10);

}
