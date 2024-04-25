#! usr/bin/env python3
import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png'))

print(os.getcwd()) # return absolute path
print(os.listdir())

print('change current working directory'.ljust(50, '.'))
os.chdir('/Users/mac/Desktop/myGitHub/Daily_Python/Python_Pandas')
print(os.getcwd())
print(os.listdir())

print('change to original working directory'.ljust(50, '.'))
os.chdir('/Users/mac/Desktop/myGitHub/Daily_Python/file_management')
print(os.getcwd())
print(os.listdir())


print(os.path.abspath('file_path.py'))  # return the absolute path of the file
print(os.path.isabs('../Python_Pandas/pokemon.csv'))  # return True if argument is absolute path; otherwise, False
print(os.path.isabs('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))

# return the relative path of the file to the target directory
print(os.path.relpath('file_path.py', '../Python_Pandas'))

# return the directory path 
print(os.path.dirname('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))
print(os.path.dirname('/Users/mac/Desktop/myGitHub/Daily_Python/file_management'))

# return the last part of the path
print(os.path.basename('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))
print(os.path.basename('/Users/mac/Desktop/myGitHub/Daily_Python/file_management'))


# return True if the path exists
print(os.path.exists('/Users/mac/Desktop/myGitHub/Daily_Python/file_management'))
print(os.path.exists('/Users/mac/Desktop/myGitHub/file_management'))

# return True if the path refers to a file
print(os.path.isfile('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))
print(os.path.isfile('/Users/mac/Desktop/myGitHub/Daily_Python/file_management'))

# return True if the path refers to a folder
print(os.path.isdir('/Users/mac/Desktop/myGitHub/Daily_Python/file_management'))
print(os.path.isdir('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))


# get the size of the file
print(os.path.getsize('/Users/mac/Desktop/myGitHub/Daily_Python/file_management/file_path.py'))

# list all the files and folders in the folder
print(os.listdir('/Users/mac/Desktop/myGitHub/Daily_Python'))

# create a new folder
print(os.getcwd())
print('Create a new folder "waffles"'.ljust(50, '.'))
os.makedirs('waffles')
print(os.listdir(os.getcwd()))