#! /usr/bin/env python3
# bullet_point_adder.py - Add bullet points to the start of each line of text on the clipboard
import pyperclip

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)


"""Copy the following list of text to try it on
Lists of animals
Lists of aquarium life
Lists of biologiests by author abbreviation
Lists of cultivars
"""

"""
AREA TO PASTE THE RESULT
"""
