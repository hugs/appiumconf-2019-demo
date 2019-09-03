/*
  i2c-mouse-driver

  - Receives commands over an I2C/TWI interface.
  - Sends data as mouse events to tethered device.

  Copyright (c) 2019 Jason Huggins
  License: MIT
*/

#include "Mouse.h"
#include <Wire.h>

void setup() {
  Mouse.begin();
  Wire.begin(8);                // join i2c bus with address #8
  Wire.onReceive(receiveEvent); // register event
}

void loop() {
  delay(100);
}

void receiveEvent(int howMany) {
  if (Wire.available()) {
    int command = Wire.read();

    // Mouse move
    if (command == 1) {
      int x = Wire.read(); 
      int y = Wire.read();
      Mouse.move(x, y);

    // Mouse press
    } else if (command == 2) {
      Mouse.press();

    // Mouse release
    } else if (command == 3) {
      Mouse.release();
    }

    // Wait
    else if (command == 4) {
      int ms = Wire.read(); 
      delay(ms);
    }
 
  }
}
