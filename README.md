# LED7Clock
HT16K33 7-segment LED clock on Raspberry Pi Zero W

This is a 2024 re-write of the 2019 version using the same hardware. Lots of things have moved on
- Rasbian/Debian 12 bookworm
- systyemd (!)
- python3
- Adafruit driver libraries

Code is meant to run inside a python venv of the unpriv "pi" user, started as a systemd service at boot.

pi@raspberrypi0W:~ $ git clone https://github.com/aott01/LED7Clock.git
pi@raspberrypi0W:~ $ cd LED7Clock/
pi@raspberrypi0W:~/LED7Clock $ python3 -m venv venv
pi@raspberrypi0W:~/LED7Clock $ . venv/bin/activate
(venv) pi@raspberrypi0W:~/LED7Clock $ pip3 install adafruit-circuitpython-ht16k33
(venv) pi@raspberrypi0W:~/LED7Clock $ chmod 755 LED7Clock.py LED7off.py
(venv) pi@raspberrypi0W:~/LED7Clock $ sudo cp LED7Clock.service /etc/systemd/system/
(venv) pi@raspberrypi0W:~/LED7Clock $ sudo systemctl daemon-reload
(venv) pi@raspberrypi0W:~/LED7Clock $ sudo systemctl enable LED7Clock.service
(venv) pi@raspberrypi0W:~/LED7Clock $ sudo systemctl start LED7Clock.service
(venv) pi@raspberrypi0W:~/LED7Clock $ deactivate
pi@raspberrypi0W:~/LED7Clock $ 


More detailed install notes are in the labnotebook of The3Bears (private) site.
