# LED7Clock
HT16K33 7-segment LED clock on Raspberry Pi Zero W

This is a re-write of the 2019 version using the same hardware. Lots of things have moved on
- Rasbian/Debian 12 bookworm
- systyemd (!)
- python3
- Adafruit driver libraries

Code is meant to run inside a python venv of the unpriv "pi" user, started as a systemd service at boot.

More detailed install notes are in the labnotebook of The3Bears (private) site.
