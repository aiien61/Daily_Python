#! /usr/bin/env python3
import re
from termcolor import colored


def show_match(regrex: object, text: str) -> None:
    try:
        print(regrex.search(text))
    except AttributeError as e:
        print(colored('No matched string found', on_color='on_red'))

# ^: text must begin with the characters; otherwise, not found 
print('begins with by ^'.center(50, '-'))
begins_with_regrex = re.compile(r'^Hello')
show_match(begins_with_regrex, 'Hello there!')
show_match(begins_with_regrex, 'He said "Hello there!"') # not found

non_begins_with_regrex = re.compile(r'Hello')
show_match(non_begins_with_regrex, 'Hello there!')
show_match(non_begins_with_regrex, 'He said "Hello there!"')

# $: text must end with the characters; otherwise, not found
print('ends with by $'.center(50, '-'))
ends_with_regrex = re.compile(r'world!$')
show_match(ends_with_regrex, 'Hello world!')
show_match(ends_with_regrex, 'Hello world') # not found

# ^$: text must begin and end with the entire specified characters; otherwise, not found
print('begins and ends with by ^$'.center(50, '-'))
all_digit_regrex = re.compile(r'^\d+$')
show_match(all_digit_regrex, '198456131415311')
show_match(all_digit_regrex, '19845613x1415311') # not found because of not full digits

# .: anything except newline
at_regrex = re.compile(r'.at') # find any single character followed by 'at'
print(at_regrex.findall('The cat in the hat sat on the flat mat.'))

at_regrex = re.compile(r'.{1,2}at')  # find any single or two consecutive characters followed by 'at'
print(at_regrex.findall('The cat in the hat sat on the flat mat.'))

text = 'First Name: Al Last Name: Sweigart'
print('hard way to find names:')
print(text.find(':'))
print(text.find(':') + 2)
print(text[12:])

print('use regular expression to find names:')
name_regrex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(name_regrex.findall(text))
mo = name_regrex.search(text)
print(mo.group(1))
print(mo.group(2))

print(' greedy vs. non greedy dot finder '.center(50, '='))
serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>') # To find out <...> this pattern as shorter as possible
print(nongreedy.findall(serve))

greedy = re.compile(r'<.*>') # To match <...> this pattern as longer as possible
print(greedy.findall(serve))