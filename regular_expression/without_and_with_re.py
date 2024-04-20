#! /usr/bin/env python3
import re

# without using regular expression to validate whether USA phone number
def is_phone_number(text: str) -> bool:
    if len(text) != 12:
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False # no area code
    if text[3] != '-':
        return False # missing dash
    
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    
    if text[7] != '-':
        return False # missing second dash
    
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # no last 4 digits
    
    return True

def find_phone_number(message: str) -> None:
    found_number = False
    for i in range(len(message)):
        chunk = message[i: i+12]
        if is_phone_number(chunk):
            print(f'Phone number found: {chunk}')
            found_number = True
    if not found_number:
        print('Could not find any phone number.')
    return None

# with regular expression
def find_phone_number_re(message: str) -> None:
    phone_number_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    print(phone_number_regrex.findall(message))

def find_first_phone_number_re(message: str) -> None:
    phone_number_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phone_number_regrex.search(message)
    print(mo.group())


if __name__ == '__main__':
    print(is_phone_number(input('Enter your phone number: ')))

    message = 'Call me at 415-555-1111 tomorrow, or at 415-555-9999 for my office.'
    find_phone_number(message)
    find_phone_number_re(message)
    find_first_phone_number_re(message)

