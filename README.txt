Required Parts:
 - Computer running MacOS 10.15 (Catalina) or XCode 11 Beta.
    (Tested with MacOS 10.14 (Mojave) running XCode 11 Beta.)
    Note: MacOS is required to install iOS 13 Beta on the iPhone. Once it's installed, however, the demo could run on any MacOS, Windows, or Linux computer that can run Appium.

 - iPhone running iOS 13 Beta
    (Tested on iPhone Xs Max)
   
 - 1x Apple Lightning to USB Cable (0.5 m)
    https://www.apple.com/shop/product/ME291AM/A/lightning-to-usb-cable-05-m
   
 - Apple Lightning to USB 3 Camera Adapter
    https://www.apple.com/shop/product/MK0W2AM/A/lightning-to-usb-3-camera-adapter
   
 - 2x Arduino Micro
    https://store.arduino.cc/usa/arduino-micro
    https://www.pololu.com/product/2188

 - 2x Micro USB Cable
    https://www.adafruit.com/product/592
    https://www.monoprice.com/product?p_id=4867
 

 - Full-sized breadboard
    https://www.adafruit.com/product/239
    https://www.jameco.com/z/BB830-Busboard-Prototype-Systems-830-Point-Solderless-Plug-in-Breadboard-with-4-Power-Rails-21-26AWG-ABS_2283767.html

 - 3 M/M Breadboard jumper wires
    https://www.sparkfun.com/products/8431
    https://www.pololu.com/product/1702

Optional:
  - USB Mouse



1) Install iOS 13 on iPhone
 - https://developer.apple.com/support/install-beta/
 - https://www.idownloadblog.com/2019/06/05/how-to-install-ios-13-ipados-beta/

2) Enable Assistive Touch
  - Open Settings on your iPhone or iPad.
  - Tap Accessibility.
  - Tap Touch under Physical and Motor.
  - Tap AssistiveTouch.
  - Tap the switch next to AssistiveTouch so it's in the green 'on' position.
  
  (From: https://www.imore.com/how-use-mouse-or-trackpad-your-iphone-or-ipad)

3) Connect Camera Adapter to iPhone

4) Connect Lightning end of Lightning cable to Camera Adapter.

5) Connect USB-A end of Lightning cable to power.

6) Connect USB-A end mouse cable into Camera Adapter
  - Move mouse around, verify cursor moves on iPhone screen.

7) Set up breadboard:
  (See doc/arduino-micro-pinout.png for pin reference)
  1) Insert Arduino Micro #1 into breadboard
  2) Insert Arduino Micro #2 into breadboard
  3) Connect ground (GND) of Micro #1 to ground (GND) of Micro #2 with black jumper wire
  4) Connect pin #2 (SDA) of Micro #1 to pin #2 (SDA) of Micro #2 with yellow jumper wire
  5) Connect pin #3 (SCL) of Micro #1 to pin #3 (SCL) of Micro #2 with orange jumper wire

8a) Upload simple-mouse-demo.ino to Arduino Micro #2:
  - Connect USB-B (micro) end of cable to Arduino Micro #2
  - Connect USB-A end of cable to computer
  - Launch Arduino IDE
  - Open simple-mouse-demo.ino
  - Make sure the correct board is selected:
    In Arduino IDE:
      Select: Tools -> Arduino/Genuino Micro
  - Make sure the correct port is selected:
    In Arduino IDE:
      Select: Tools -> Port -> (id of connected Arduino. e.g. "/dev/cu.usbmodem14101")
  - Click the Upload button
  - After upload is done, verify the cursor moves up/down/left/right in a loop on your computer screen.

8b) Verify iPhone mouse control works with Arduino:
  - Disconnect USB-A end of cable from computer
  - Connect cable to Camera Adapter
  - Verify that Lighting cable is plugged into Camera Adapter's Lightning cable port
  - Verify that the other end of Lightning cable is connected to power.
  - Verify that the cursor is moving up/down/left/right on the iPhone screen.
  - After verification is complete, disconnect USB-A end of cable from Camera Adapter.


9) Upload i2c-mouse-driver.ino to Arduino Micro #2:
  - Connect USB-A end of cable to computer.
  - Open i2c-mouse-driver.ino in Arduino IDE
  - Make sure the correct board is selected in Arduino IDE:
    In Arduino IDE:
      - Tools -> Arduino/Genuino Micro
  - Click the Upload button
  - After Upload is done, disconnect USB-A end of cable from computer


10) Upload Standard Firmata to Arduino Micro #1:
  - Using your second USB-B micro to USB-A cable, connect USB-B (micro) end of cable to Arduino Micro #1
  - Connect USB-A end of cable to computer
  - Open StandardFirmata.ino
    - In Arduino IDE:  
      Select: File -> Examples -> Firmata -> Standard Firmata
  - Make sure the correct port is selected:
    In Arduino IDE:
      Select: Tools -> Port -> (id of connected Arduino. e.g. "/dev/cu.usbmodem14101")
  - Click the Upload button
  - After Upload is done, keep USB-A end of cable connected to computer  



11) Get appium-arduino-driver
  - Download code (In a terminal window on your computer):
      git clone https://github.com/hugs/appium-arduino-driver.git
  - Install
      npm install
      
      
12) Run the server:
  - Connect USB-A end of cable connected to Arduino Micro #2 to Camera Adapter
      
  - Start Server (In a terminal window on your computer):
    node .

  - You should see the following in your terminal window:
      "info Arduino ArduinoDriver server listening on http://localhost:4847"
      
13) Install Angry Birds on iPhone:
  - On iPhone, open App Store
  - Search for "Angry Birds Classic"
  - Install

  
14) Set-up and activate Python environment:
  - Download code (In a terminal window on your computer):
      git clone https://github.com/hugs/AppiumConf-2019-Demo
      
  cd AppiumConf-2019-Demo/demo
  python3 -m venv env
  source env/bin/activate
  pip install -r requirements.txt
  
15) Run Angry Birds demo:
  python angry-birds.py
  
16) Deactivate Python environment:
  In AppiumConf-2019-Demo/demo:
    deactivate
  



