#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|P|i|e|P|i|e|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2022, piepie.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# grove_gpio12.py
# Blinking led without warning (Add try/except)
#
# Author : sosorry
# Date   : 2023/05/30

import RPi.GPIO as GPIO 
import time

LED_PIN = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        print("LED is on")
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(2)
        print("LED is off")
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(2)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
finally:
    GPIO.cleanup()  


