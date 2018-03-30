#!/usr/bin/python
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|R|a|s|p|b|e|r|r|y|P|i|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2018, raspberrypi.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# grove_gpio12.py
# Blinking led without warning (Add try/except)
#
# Author : sosorry
# Date   : 06/22/2014

import RPi.GPIO as GPIO 
import time

# for ReSpeaker 2-Mic HAT
# https://www.raspberrypi.com.tw/17528/71001/
RELAY_PIN = 32
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


