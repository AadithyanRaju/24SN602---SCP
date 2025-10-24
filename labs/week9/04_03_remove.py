"""
CAUTION
Deleting anything with python will permanently delete the file!
You will not be able to recover anything you delete with python!
USE CAUTION!
CAUTION

Use Path.rmdir() and Path.unlink() to delete a folder and file respectively

"""

from pathlib import Path
import os

path = Path.cwd()
print(f'Current Working Directory: {path}')
print('New dir A is created')
new_dir = path / 'A'
new_dir.mkdir(exist_ok=True)
#ls
print(os.listdir(path))
print('New file test.txt is created in A')
new_file = new_dir / 'test.txt'
new_file.touch(exist_ok=True)
#ls
print(os.listdir(new_dir))
print('File test.txt is deleted')
new_file.unlink()
#ls
print(os.listdir(new_dir))
print('Directory A is deleted') 
new_dir.rmdir()
#ls
print(os.listdir(path))

