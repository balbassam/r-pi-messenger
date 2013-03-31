#!/usr/bin/python

from time import sleep
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

import smbus
import sys
import re

# initialize the LCD plate
# use busnum = 0 for raspi version 1 (256MB) and busnum = 1 for version 2
lcd = Adafruit_CharLCDPlate(busnum = 0)

# Clear the text on the LCD and turn on the backlight
while not(lcd.buttonPressed(lcd.SELECT)):
    lcd.backlight(lcd.OFF)
    sleep(0.5)
    lcd.backlight(lcd.ON)
    sleep(0.5)
