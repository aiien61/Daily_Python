#! /usr/bin/env python3

# raw string
print('This is a Carol\'s cat.')
print(r'This is a Carol\'s cat.')

# upper() & lower()
spam = 'Hello world'
spam = spam.upper()
print(spam)
spam = spam.lower()
print(spam)

# title() & capitalize()
spam = spam.capitalize()
print(spam)
spam = spam.title()
print(spam)

# isupper() & islower()
spam = 'Hello world'
print(spam.islower())  # false
print(spam.isupper())  # false
print('HELLO'.isupper())  # true
print('world'.islower())  # true
print('abc12345'.islower())  # true
print('ABC12345'.isupper())  # true
print('12345'.islower())  # false
print('12345'.isupper())  # false

# isalpha(): whether letters only
print('hello'.isalpha())  # true
print('hello123'.isalpha())  # false

# isalnum(): whether letters or number is contained only
print('abc123'.isalnum())  # true
print('123'.isalnum())  # true
print('abc'.isalnum())  # true

# isdecimal(): whether numbers only
print('123'.isdecimal())  # true
print('abc'.isdecimal())  # false
print('abc123'.isdecimal())  # false


# isspace(): whether whitespace only
print('   '.isspace())  # true
print('  abc   '.isspace())  # false

# istitle(): whether titlecase only
print('This Is Title Case'.istitle())  # true
print('This Is Title Case 123'.istitle())  # true
print('This Is not Title Case'.istitle())  # false
print('This Is NOT Title Case Either'.istitle())  # false

# startwith() & endwith()
print('Hello World!'.startswith('Hello'))  # true
print('Hello World!'.endswith('World!'))  # true
print('Hello World!'.endswith('World'))  # false
print('abc123'.startswith('abcd'))  # false
print('abc123'.endswith('123'))  # true
print('Hello World!'.startswith('Hello World!'))  # true
print('Hello World!'.endswith('Hello World!'))  # true

# join() & split()
print(', '.join(['cats', 'rats', 'bats']))
print(' '.join(['My', 'name', 'is', 'Simon']))
print('->'.join(['stopA', 'stopB', 'stopC']))
print('My name is Simon'.split())
print('stopA->stopB->stopC'.split('->'))
print('My name is Simon'.split('m'))

# rjust() & ljust() & center()
print('hello'.rjust(10))
print('hello'.rjust(20))
print('hello world'.rjust(20))
print('hello'.ljust(10))
print('0123456789'.rjust(10))
print('123456789'.rjust(10))
print('9'.rjust(10))
print('0123456789'.ljust(10))
print('012345678'.ljust(10))
print('0'.ljust(10))
print('hello'.rjust(20, '*'))
print('hello'.ljust(20, '.'))
print('hello'.center(20, '-'))
print('hello'.center(20))

# strip() & rstrip() & lstrip()
spam = '   hello world   '
print(spam.strip())
print(spam.lstrip())
print(spam.rstrip())
spam = 'SpamSpamBaconSpamEggsSpamSpam'
print(spam.strip('ampS')) # from both side to find a, m, p, S, and delete them recursively

# replace()
spam = 'hello world'
print(spam.replace('rld', 'ods'))

import pyperclip
pyperclip.copy('hello world')
print(pyperclip.paste())