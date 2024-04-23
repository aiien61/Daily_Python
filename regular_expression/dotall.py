#! /usr/bin/env python3
import re

prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'

print(' find anything except for newline '.center(100, '='))
dot_regrex = re.compile(r'.*')
print(dot_regrex.search(prime))

print(' use DOTALL to find anything as longer as possible including newline '.center(100, '='))
dot_regrex = re.compile(r'.*', re.DOTALL)
print(dot_regrex.search(prime))

print(' use IGNORECASE to disable case-sensitive '.center(100, '='))
vowel_regrex = re.compile(r'[aeiou]')
print(vowel_regrex.findall('Robocop Eats Baby Food. BABY FOOD.'))
vowel_regrex = re.compile(r'[aeiou]', re.IGNORECASE)
print(vowel_regrex.findall('Robocop Eats Baby Food. BABY FOOD.'))
vowel_regrex = re.compile(r'[aeiou]', re.I)  # re.I = re.IGNORECASE
print(vowel_regrex.findall('Al, why does your programming book talk about robocop so much?'))

robocop_regrex = re.compile(r'robocop', re.I)
print(robocop_regrex.search('Robocop is part man, part machine, all cop.').group())
print(robocop_regrex.search('ROBOCOP protects the innocent.').group())
print(robocop_regrex.search('Al, why does your programming book talk about robocop so much?').group())
