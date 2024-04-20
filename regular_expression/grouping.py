#! /usr/bin/env python3
import re

message = 'my number is 123-505-1111'

pattern = r'\d\d\d-\d\d\d-\d\d\d\d'
regrex = re.compile(pattern)
mo = regrex.search(message)  # matching object
print(mo.group())

pattern = r'(\d\d\d)-(\d\d\d-\d\d\d\d)'  # divided into 2 groups
regrex = re.compile(pattern)
mo = regrex.search(message)
print(mo.group())
print(mo.group(1))
print(mo.group(2))

pattern = r'\(\d\d\d\) \d\d\d-\d\d\d\d'  # search include parenthese
regrex = re.compile(pattern)
mo = regrex.search('my number is (123) 505-1111')
print(mo.group())
