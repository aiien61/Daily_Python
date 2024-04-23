#! usr/bin/env python3
import re

# Find '42', '1,234', '6,368,745' but not '12,34,567' or '1234'
num_regrex = re.compile(r'^(\d{1,3})(,\d{3})*$')

print(num_regrex.search('6,368,745'))
print(num_regrex.search('1234'))

# Find 'Satoshi Nakamoto', 'Alice Nakamoto', 'Robocop Nakamoto'
# but not 'satoshi Nakamoto', 'Mr. Nakamoto', 'Satoshi nakamoto'

name_regrex = re.compile(r'[A-Z]([a-z]*|^.) Nakamoto')
better_name_regrex = re.compile(r'[A-Z][a-z]*\sNakamoto')

print(better_name_regrex.search('Robocop Nakamoto'))
print(better_name_regrex.search('Mr. Nakamoto'))

# Find a sentence with three parts; first part can only be 'Alice', 'Bob', or 'Carol',
# and the second part can only be 'eats', 'pets', or 'throws', and the last part can only be
# 'apples', 'cats', or 'baseballs'

regrex = re.compile(r'''
(Alice|Bob|Carol)
\s
(eats|pets|throws)
\s
(apples|cats|baseballs)
\.
''', re.VERBOSE | re.IGNORECASE)

print(regrex.search('Alice eats apples.'))
print(regrex.search('Bob pets cats.'))
print(regrex.search('Alice throws Apples.'))
print(regrex.search('BOB PETS CATS.'))

print(regrex.search('Alice eats apples'))
print(regrex.search('Robocop eats apples'))
print(regrex.search('ALICE THROWS FOOTBALLS.'))
print(regrex.search('Carol pets 7 cats.'))
