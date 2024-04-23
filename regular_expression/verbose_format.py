#! /usr/bin/env python3
import re


# hard to read and interpret
phone_regrex = re.compile(r'\(\d\d\d\)(-)\d\d\d-\d\d\d\d')  # example: (000)-555-5555

# easier to read and interpret
phone_regrex = re.compile(r'''
(\d{3}-|                        # area code
\(\d{3}\))?                     # -or- area code with parenthese and no dash
\d{3}                           # first 3 digits
-                               # second dash
\d{4}                           # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,4})?    # extension, like x1234
''', re.VERBOSE)

print(phone_regrex.search('Find him at 000-555-5555 x1234.').group())
