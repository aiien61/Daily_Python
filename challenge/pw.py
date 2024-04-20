#! /usr/bin/env python3
import sys
import pyperclip

PASSWORDS = {
    'email': 'aldfjklksdnfknvoias',
    'blog': 'ajsdvlkaklvm',
    'luggage': '12345'
}

try:
    account = sys.argv[1]
except IndexError:
    print('Usage: python3 pw.py <account>')
    sys.exit()

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print(f'Password for {account} copied to clipboard.')
else:
    print(f'There is no account named {account}')
