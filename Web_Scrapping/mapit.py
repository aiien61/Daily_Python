#! /usr/bin/env python3
# mapit.py - Launches a map in the browser using an address from the command line or clipboard
# Usage: python3 mapit.py <address> - Launches a map to the address on the command line
#        python3 mapit.py - Get address from the clipboard and launches a map

import sys
import pyperclip
import webbrowser

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)

