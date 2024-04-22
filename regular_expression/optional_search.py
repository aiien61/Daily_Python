import re
from termcolor import colored

def show_search(match_object: object) -> None:
    try:
        print(match_object.group())
    except AttributeError as e:
        print(colored('no matched string found', on_color='on_red'))
    return None

# ?: to match zero or only appearing once
print('?'.center(20, '-'))
bat_regrex = re.compile(r'Bat(wo)?man')

mo = bat_regrex.search('The Adventures of Batman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwoman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwowowoman')
show_search(mo)

phone_regrex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_regrex.search('My phone is 415-555-1234')
show_search(mo)

mo = phone_regrex.search('My phone is 555-1234')
show_search(mo)
print(mo == None)

phone_regrex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phone_regrex.search('My phone is 415-555-1234')
show_search(mo)

mo = phone_regrex.search('My phone is 555-1234')
show_search(mo)

# *: to match zero or more times
print('*'.center(20, '-'))
bat_regrex = re.compile(r'Bat(wo)*man')
mo = bat_regrex.search('The Adventures of Batman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwoman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwowowoman')
show_search(mo)

# +: match one or more times
print('+'.center(20, '-'))
bat_regrex = re.compile(r'Bat(wo)+man')
mo = bat_regrex.search('The Adventures of Batman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwoman')
show_search(mo)

mo = bat_regrex.search('The Adventures of Batwowowoman')
show_search(mo)

# search for ?, *, + using escape
print('search for question mark, asterisk, or plus'.center(50, '-'))
regrex = re.compile(r'\+\*\?')
mo = regrex.search('I learn about +*? regrex syntax')
show_search(mo)

regrex = re.compile(r'(\+\*\?)+')
mo = regrex.search('I learned about +*?+*?+*?+*?+*?+*?+*?+*? regrex syntax')
show_search(mo)

# {x}: to match a specific number of repetition of a group
print('{}'.center(20, '-'))
regrex = re.compile(r'(ha){3}')
mo = regrex.search('He said "hahaha')
show_search(mo)

# find out exactly 3 times of this pattern
phone_regrex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phone_regrex.search('My numbers are 415-555-1234,555-3232,212-555-0000')
show_search(mo)

# {x, y}: to mathc at least x times and at most y times of repetition of a group
print('{x,y}'.center(20, '-'))
regrex = re.compile(r'(ha){3,5}')
mo = regrex.search('He said "haha')
show_search(mo)

mo = regrex.search('He said "hahaha')
show_search(mo)

mo = regrex.search('He said "hahahahaha')
show_search(mo)

# {x, }: to match at least x times of repetition of a group
print('{x,}'.center(20, '-'))
regrex = re.compile(r'(ha){3,}')
mo = regrex.search('He said "haha')
show_search(mo)

mo = regrex.search('He said "hahaha')
show_search(mo)

mo = regrex.search('He said "hahahahahahahahahahahahahahahahahahahaha')
show_search(mo)

# greedy and nongreedy matching
print('greedy matching'.center(30, '-'))
greedy_regrex = re.compile(r'(ha){3,5}')
mo = greedy_regrex.search('hahahahaha')
show_search(mo)

digit_regrex = re.compile(r'(\d){3,5}')
mo = digit_regrex.search('1234567890|0987654321')
show_search(mo)

print('nongreedy matching'.center(30, '-'))
nongreedy_regrex = re.compile(r'(ha){3,5}?')
mo = nongreedy_regrex.search('hahahahaha')
show_search(mo)

digit_regrex = re.compile(r'(\d){3,5}?')
mo = digit_regrex.search('1234567890|0987654321')
show_search(mo)
