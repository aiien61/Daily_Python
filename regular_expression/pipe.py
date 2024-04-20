#! /usr/bin/env python3
import re

pattern = r'batman|spider man'
hero_regrex = re.compile(pattern)
mo = hero_regrex.search('batman and spider man')
print(mo.group())
mo = hero_regrex.search('spider man and batman')
print(mo.group())

pattern = r'(super|snow|bat|spider|iron)man'
man_regrex = re.compile(pattern)
mo = man_regrex.search('we made a snowman.')
print(mo.group())

mo = man_regrex.search('batman\'s new series is coming')
print(mo.group())

mo = man_regrex.search('aquaman is a hero.')
print(mo == None)
print(mo.group())
