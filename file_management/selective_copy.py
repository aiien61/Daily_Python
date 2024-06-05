#! /usr/bin/env python3
# selective_copy.py - Copy files with certain extensions
# Usage: python3 selective_copy.py <source> <extensions> - Copy files with certain extensions
#        python3 selective_copy.py <source> - Copy files with .pdf and .jpg extensions

import os, sys, shutil
from typing import List

def selective_copy(source: str, extensions: List[str]=['.pdf', '.jpg']) -> None:
    os.mkdir(f'{source}_backup')
    for foldername, subfolders, filenames in os.walk(source):
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                shutil.copy(os.path.join(foldername, filename), f'{source}_backup')
    return None


if __name__ == '__main__':
    source = sys.argv[1]
    if len(sys.argv) == 3:
        selective_copy(source, sys.argv[2:])
    else:
        selective_copy(source)