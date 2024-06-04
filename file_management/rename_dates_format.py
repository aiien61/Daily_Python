#! /usr/bin/env python3
# rename_dates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY
import os, sys, re, shutil

pattern_us = re.compile("""
# File format: xxxxMM-DD-YYYYxxxx.xxx
                        
# prefix word-part of filename
^(.*?)
                        
# MM
([01]?\d)

# separator between MM and DD
(-|/)
                        
# DD
([0123]?\d)
                        
# separator between DD and YYYY
(-|/)

# YYYY                        
(19\d{2}|20\d{2})
                        
# suffix word-part of filename
(.*?)$
""", re.VERBOSE)

us_regex = re.compile(pattern_us)

for folder, subfolders, filenames in os.walk(os.getcwd()):
    for us_filename in filenames:
        mo = us_regex.search(us_filename)

        # Skip files without a date in the filename.
        if mo == None:
            continue

        # Get the different parts of the filename.
        prefix = mo.group(1)
        suffix = mo.group(7)
        month = '0' + mo.group(2) if len(mo.group(2)) == 1 else mo.group(2)
        day = '0' + mo.group(4) if len(mo.group(4)) == 1 else mo.group(4)
        year = mo.group(6)
        separator = mo.group(3)
        
        # Form the European style filename.
        date_eu = f'{separator}'.join([day, month, year])
        eu_filename = prefix + date_eu + suffix
        
        # Get the full, absolute file paths.
        us_file_path = os.path.join(folder, us_filename)
        eu_file_path = os.path.join(folder, eu_filename)
        
        # Rename the files.
        shutil.move(us_file_path, eu_file_path)
