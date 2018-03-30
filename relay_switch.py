#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2018, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# relay_switch.py
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO 
import time

RELAY_PIN = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(RELAY_PIN, GPIO.OUT, initial=GPIO.HIGH)

try:
    while True:
        print("Relay is on")
        GPIO.output(RELAY_PIN, GPIO.LOW)
        time.sleep(2)
        print("Relay is off")
        GPIO.output(RELAY_PIN, GPIO.HIGH)
        time.sleep(2)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.cleanup()  


