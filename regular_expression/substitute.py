#! /usr/bin/env python3
import re

print(' Hide he name using sub '.center(50, '='))
classified = 'Agent Bob gave the secret documents to Agent Alice.'

hide_names_regrex = re.compile(r'Agent \w+')
print(hide_names_regrex.findall(classified))
print(hide_names_regrex.sub('CENSORED', classified))

# only redact name of agent but keep the title 'agent'
hide_names_regrex = re.compile(r'Agent (\w)(\w+)')
print(hide_names_regrex.findall(classified))
# only keep the group 1 original
print(hide_names_regrex.sub(r'Agent \1*****', classified)) 

# only keep the group 2 original
print(hide_names_regrex.sub(r'Agent *\2', classified))
