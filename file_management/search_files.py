#! /usr/bin/env python3
# search_files.py - search files in specified directory and search text using regular expression
# Usage: python3 search_files.py <directory> <regular expression>

import os, sys, re

print(f'User regex pattern: {sys.argv[2:]}')
pattern = ''.join(sys.argv[2:])
regex = re.compile(r'{}'.format(pattern))

for folder, subfolders, files in os.walk(sys.argv[1]):
    for filename in files:
        if filename.endswith('txt'):
            filepath = os.path.join(folder, filename)
            with open(filepath, 'r') as textfile:
                if result :=regex.search(textfile.read()):
                    print(f'"{result.group()}" found in {filepath}')
