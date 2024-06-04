#! /usr/bin/env python3
# search_files.py - search files in specified directory and search text using regular expression
# Usage: python3 search_files.py <directory> <regular expression>

import os, sys, re

for folder, subfolders, files in os.walk(sys.argv[1]):
    for file in files:
        pass