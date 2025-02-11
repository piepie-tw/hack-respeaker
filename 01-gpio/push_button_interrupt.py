#!/usr/bin/python3
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|P|i|e|P|i|e|.|c|o|m|.|t|w|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+
# Copyright (c) 2022, piepie.com.tw
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
#
# push_button_interrupt.py
# Response when push button is pressed with interrupt way, and de-bounces 
# by software
#
# Author : sosorry
# Date   : 2023/05/30

import RPi.GPIO as GPIO                 
import time

GPIO.setmode(GPIO.BOARD)                
BTN_PIN = 11
WAIT_TIME = 200
GPIO.setup(BTN_PIN, GPIO.IN)

def mycallback(channel):                                                 
    print("Button pressed @", time.ctime())

try:
    GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, callback=mycallback, bouncetime=WAIT_TIME)

    while True:
        time.sleep(10)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()          
