#! /usr/bin/env python3
# search_files_size.py - search for files that are larger than a certain size (bytes)
# Usage: python3 search_files_size.py <directory> <size>
import os, sys, copy
from enum import Enum, auto

class Filesize(Enum):
    bytes = auto()
    KB = auto()
    MB = auto()
    GB = auto()
    TB = auto()


def get_size_bound(size: str) -> tuple:
    if 'k' in size:
        unit = Filesize.KB
        size, _ = size.split('k')
    elif 'm' in size:
        unit = Filesize.MB
        size, _ = size.split('m')
    elif 'g' in size:
        unit = Filesize.GB
        size, _ = size.split('g')
    elif 't' in size:
        unit = Filesize.TB
        size, _ = size.split('t')
    elif 'b' in size:
        unit = Filesize.bytes
        size, _ = size.split('b')
    else:
        unit = Filesize.bytes

    bytesize = int(size) * 1024 ** (unit.value - 1)
    return bytesize, Filesize.bytes


def search_files(directory: str, size: str):
    sizebound, sizeunit = get_size_bound(size.lower())
    for folder, subfolders, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(folder, filename)
            filesize = os.path.getsize(filepath)
            unit = copy.copy(sizeunit)
            if filesize > sizebound:
                while True:
                    quotient, remainder = divmod(filesize, 1024)
                    if quotient == 0:
                        break
                    filesize = filesize / 1024
                    unit = Filesize(unit.value + 1)

                print(f'{filepath} - {filesize} {unit.name}')

if __name__ == '__main__':
    search_files(sys.argv[1], sys.argv[2])
