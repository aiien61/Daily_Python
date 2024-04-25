#! usr/bin/env python3
import os

def get_total_files_size(path: str) -> int:
    total_size = 0
    for filename in os.listdir(path):
        filepath = os.path.join(path, filename)
        if not os.path.isfile(filepath):
            continue

        total_size += os.path.getsize(filepath)

    return total_size

if __name__ == '__main__':
    print(get_total_files_size(os.getcwd()))
