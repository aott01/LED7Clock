#!/home/pi/LED7Clock/venv/bin/python3

import board
import busio
import syslog
from adafruit_ht16k33 import segments

# Create the I2C interface.
i2c = busio.I2C(board.SCL, board.SDA)
# Create the LED segment class.
# This creates a 7 segment 4 character display, default address=0x70:
myDisplay = segments.Seg7x4(i2c)

syslog.syslog("turning off display with LED7off.py")

# Clear the display.
myDisplay.fill(0)

# ==========================================================================
# turn off display by writing ' ' space to all four segments, turn colon off
# ==========================================================================
myDisplay[0] = ' '
myDisplay[1] = ' '
myDisplay[2] = ' '
myDisplay[3] = ' '
myDisplay.colon = False
myDisplay.brightness=0
myDisplay.show()

###
