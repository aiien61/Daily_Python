#! /usr/bin/env python3
# backup_to_zip.py - Copies an entire folder and its contents into 
# a ZIP file whose filename increments.

import zipfile, os

def backup_to_zip(folder: str):
    # Backup the entire contents of "folder" into a ZIP file.
    folder = os.path.abspath(folder)

    # figure out the filename this code should use based on what files already exist
    number = 1
    while True:
        zip_filename = f'{os.path.basename(folder)}_{number}.zip'
        if not os.path.exists(zip_filename):
            break
        number += 1

    # Create the ZIP file
    print(f'Creating {zip_filename}...')
    backup_zip = zipfile.ZipFile(zip_filename, 'w')

    # Walk the entire folder tree and compress the files in each folder
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file
        backup_zip.write(foldername)

        # Add all the files in this folder to the ZIP file
        for filename in filenames:
            newbase = os.path.basename(folder) + '_'
            
            # Don't backup the backup ZIP files
            if filename.startswith(newbase) and filename.endswith('.zip'):
                continue


            backup_zip.write(os.path.join(foldername, filename))
    
    backup_zip.close()
    print('Done.')

if __name__ == '__main__':
    backup_to_zip('delicious')