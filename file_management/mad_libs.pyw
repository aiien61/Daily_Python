#! /usr/bin/env python3
# mad_libs.pyw - Loads text file and replaces words with user input
# Usage: python3 mad_libs.pyw
import shelve

text = """\
The {ADJECTIVE} panda walked to the {NOUN1} and then {VERB}. \
A nearby {NOUN2} was unaffected by these events.\
"""

shelf = shelve.open('mad_libs')
shelf['ADJECTIVE'] = None
shelf['NOUN1'] = None
shelf['VERB'] = None
shelf['NOUN2'] = None

key = input('Enter your name:\n')
adj = input('Enter an adjective:\n')
noun1 = input('Enter a noun:\n')
verb = input('Enter a verb:\n')
noun2 = input('Enter a noun:\n')

text = text.format(ADJECTIVE=adj, NOUN1=noun1, VERB=verb, NOUN2=noun2)

print(text)
shelf[key] = text
shelf.close()

with open(f'{key}.txt', 'w') as f:
    f.write(text)
