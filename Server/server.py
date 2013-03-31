#!/usr/bin/python

# Functionality to allow the LCD display to work
from time import sleep
from Adafruit_I2C import Adafruit_I2C
from Adafruit_MCP230xx import Adafruit_MCP230XX
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Function to format the message to fit in the LCD
def formatForLCD(Text):
    # Formats text so it fits in the LCD
    res = []
    for i in range(0,len(Text), 32):
        res.append( Text[i:i + 16] + "\n" + Text[i+16:i+32] )
    return res

# http://stackoverflow.com/questions/5419888/reading-from-a-frequently-updated-file
def readFile():
     inFile = open('/var/www/Messages.txt','r')
     Messages = inFile.readlines()
     return Messages
     inFile.close()

# initialize the LCD plate
# use busnum = 0 for raspi version 1 (256MB) and busnum = 1 for version 2
lcd = Adafruit_CharLCDPlate(busnum = 0)

# Clear the text on the LCD and turn on the backlight
lcd.clear()
lcd.backlight(lcd.ON)

# Read the messages file
Messages = readFile()
Message = formatForLCD(Messages[0])

lcd.clear()
lcd.message("Welcome")

index = 0
CurMsg = 0

# Loop this indefinatly to re-act when a button is pressed
while 1:
    # Go to the previous message
    if (lcd.buttonPressed(lcd.UP)):
        CurMsg -= 1
        if(CurMsg < 0 or CurMsg >= len(Messages) ):
            CurMsg = 0
        Message = formatForLCD(Messages[CurMsg])
        index = 0
        lcd.clear()
        lcd.message(Message[index])
        sleep(.5)

    # Go to the next message
    if (lcd.buttonPressed(lcd.DOWN)):
        CurMsg += 1
        if(CurMsg >= len(Messages)):
            CurMsg = len(Messages) -1
        Message = formatForLCD(Messages[CurMsg])
        index = 0
        lcd.clear()
        lcd.message(Message[index])
        sleep(.5)

    # Scroll backwards through current message
    if (lcd.buttonPressed(lcd.LEFT)):
	lcd.clear()
	index -= 1
        if(index < 0):
           index = 0
	lcd.message(Message[index])
        sleep(.5)

    # Scroll forwards through current message
    if (lcd.buttonPressed(lcd.RIGHT)):
	lcd.clear()
	index += 1
        if(index >= len(Message)):
           index = len(Message)-1
	lcd.message(Message[index])
        sleep(.5)
        
    # Get new messages
    if (lcd.buttonPressed(lcd.SELECT)):
        lcd.clear()
        lcd.message("Re-reading Files\n")
        sleep(1.1)
        Messages = readFile()
        lcd.clear()
        Message = formatForLCD(Messages[0])
	lcd.message(Message[0])

# I hope that we never arrive here
lcd.message("Something just\nwent wrong")
