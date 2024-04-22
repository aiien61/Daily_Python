#! /usr/bin/env python3
import re
from termcolor import colored

def show_match(match_object: object) -> None:
    try:
        print(match_object.group())
    except AttributeError as e:
        print(colored('No matched string found', on_color='on_red'))


print('search vs. findall'.center(50, '='))
print('search'.center(30, '-'))
# search(): find the first matched one that meets the condition
phone_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phone_regrex)
mo = phone_regrex.search('Cell: 415-555-9999 Work: 212-555-0000')
show_match(mo)

print('findall'.center(30, '-'))
# findall(): find the all matched results that all meet the condition and return them in a list
print('no groups in pattern')
phone_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo = phone_regrex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

print('groups in pattern')
phone_regrex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # has groups
mo = phone_regrex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

phone_regrex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')  # has groups
mo = phone_regrex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo)

# \d: any numeric digit from 0 to 9
# \D: any character that is not a numeric digit from 0 to 9
# \w: any letter, numeric digit, or the underscore character ( think of this as matching 'word' characters )
# \W: any character that is not a letter, numeric digit, or the underscore character
# \s: any space, tab, or newline character ( think of this as matching 'space' characters )
# \S: any character that is not a space, tab, or newline
print('='*30)
digi_regrex = re.compile(r'\d') # easier
print(digi_regrex.search('welcome to 7-11'), 'matched by \d')
digi_regrex = re.compile(r'(0|1|2|3|4|5|6|7|8|9)') # a lot more effort
print(digi_regrex.search('welcome to 7-11'), 'matched by (0|1|2|3|4|5|6|7|8|9)')

lyrics = """
12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a miling, \
7 swans a swimming, 6 geese a laying, 6 golden rings, 4 calling birds, 3 french hens, 2 turtle doves, \
and 1 partridge in a pear tree
"""
print(lyrics)
print('Grouping all things and the number of them in the lyrics:')
xmas_regrex = re.compile(r'\d\s\w+')
print(xmas_regrex.findall(lyrics))

print('making our own character classes'.center(50, '-'))
vowel_regrex = re.compile(r'[aeiou]')  # same as '(a|e|i|o|u)'
print(vowel_regrex.findall('Robocop eats baby food. BABY FOOD.'))

vowel_regrex = re.compile(r'[aeiouAEIOU]')
print(vowel_regrex.findall('Robocop eats baby food. BABY FOOD.'))

vowel_regrex = re.compile(r'[a-fA-F]')
print(vowel_regrex.findall('Robocop eats baby food. BABY FOOD.'))

double_vowl_regrex = re.compile(r'[aeiouAEIOU]{2}') # find consecutive vowels
print(double_vowl_regrex.findall('Robocop Eats Baby Food. BABY FOOD.'))

# ^: exclude the specified characters
print('Negative character classes'.center(50, '-'))
consonant_regrex = re.compile(r'[^aeiouAEIOU]')
print(consonant_regrex.findall('Robocop Eats Baby Food. BABY FOOD.'))
