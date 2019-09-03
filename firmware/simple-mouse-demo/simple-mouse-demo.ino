/*
  simple-mouse-demo

  Simple demo to control the mouse from an Arduino Micro.

  Copyright (c) 2019 Jason Huggins
  License: MIT

  Reference:
  http://www.arduino.cc/en/Tutorial/KeyboardAndMouseControl
*/

#include "Mouse.h"

void setup() {
  // Initialize mouse control:
  Mouse.begin();
}

void loop() {  
  // Move mouse up
  Mouse.move(0, -20);
  delay(1000); 
  
  // Move mouse down
  Mouse.move(0, 20);
  delay(1000); 

  // Move mouse left
  Mouse.move(-20, 0);
  delay(1000); 

  // Move mouse right
  Mouse.move(20, 0);
  delay(1000); 

  // Perform mouse left click
  // Note: Depending on where the mouse cursor is at the time,
  // this might not be a safe command to run.
  // Uncomment the following code if you're feeling lucky:
  ////--------------
  //Mouse.press();
  //delay(200);
  //Mouse.release();
  //delay(1000); 
  ////-------------- 
}
