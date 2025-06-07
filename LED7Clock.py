#!/home/pi/LED7Clock/venv/bin/python3

# rewrite
# still standalone, no web control, need to set TZ varialbe at OS

# ===========================================================================
# Clock with 24-hr time, brightness dims during the night
# ===========================================================================

import board
import busio
import datetime
import os
import socket
import syslog
import time
from adafruit_ht16k33 import segments

# create the I2C interface
i2c = busio.I2C(board.SCL, board.SDA)
# This creates a 7 segment 4 character display, at default address=0x70:
display = segments.Seg7x4(i2c)

syslog.syslog("starting LED7clock.py")

# show IP on display
gw = os.popen("/usr/sbin/ip -4 route show default").read().split()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((gw[2], 0))
ipaddr = s.getsockname()[0]
#gateway = gw[2]
#host = socket.gethostname()
#print ("IP:", ipaddr, " GW:", gateway, " Host:", host)
display.marquee("IP "+ipaddr, delay=0.4, loop=False)

# print timezone, requires it to be set on the OS
zonename = os.environ["TZ"]
display.marquee(zonename, delay=0.3, loop=False)

# time sync status
# /usr/bin/timedatectl | grep <>
# one time shot, 1 second delay, then try again
ret = os.system('/usr/bin/timedatectl | /usr/bin/grep -q "System clock synchronized: yes"')
if ret > 0:
  syslog.syslog("System clock synchronized: no")
  display.marquee("not synced", delay=0.4, loop=False)
  time.sleep(1)
else:
  syslog.syslog("System clock synced, also checking NTP service, return was "+str(ret))
  display.marquee("synced", delay=0.4, loop=False)
ret = os.system('/usr/bin/timedatectl | /usr/bin/grep "NTP service: active"')
if ret == 0:
  display.marquee("ntp yes", delay=0.4, loop=False)

# Clear the display
display.fill(0)

while(True):
  now = datetime.datetime.now()
  hour = now.hour
  minute = now.minute
  second = now.second

  if hour > 20 :
    display.brightness=0.2
  elif hour < 6:
    display.brightness=0.2
  elif hour > 6 :
    display.brightness=0.8

  # Set hours
  display[0]=str(int(hour / 10))        # Tens
  display[1]=str(hour % 10)             # Ones
  # Set minutes
  display[2]=str(int(minute / 10))      # Tens
  display[3]=str(minute % 10)           # Ones
  # Toggle colon
  display.colon=bool(second % 2)# Toggle colon at 1 second even/odd

  # Wait a half second (less than 1 second, to prevent colon blinking getting
  # delayed by other processes on single core CPU)
  time.sleep(0.5)

display.fill(0)
#try to log on exit
syslog.syslog("exiting LED7clock.py")
###
