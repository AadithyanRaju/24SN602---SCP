"""
Use pathlib.Path objects to 

a) create a new directory
b) create a new file
c) move a file from your current directory into the new directory

use shutil to
d) copy the file back into the original location (while keeping it in the new directory)

"""

from pathlib import Path
import os
import shutil

path = Path.cwd()
while True:
    print('''
-----MENU-----
1. Print Working Directory 
2. List Working Directory
3. Create New Directory
4. Create New File
5. Move File to New Directory
6. Copy File Back to Original Location
7. Exit
--------------''')
    ch = int(input('Enter Choice: '))
    if ch == 7: break
    elif ch == 1: print(path.cwd())
    elif ch == 2: print(os.listdir(path))
    elif ch == 3: 
        new_dir = input('Enter new directory name: ')
        (path / new_dir).mkdir(exist_ok=True)
    elif ch == 4: 
        new_file = input('Enter new file name: ')
        (path / new_file).touch(exist_ok=True)
    elif ch == 5: 
        file_to_move = input('Enter file name to move: ')
        if (path / file_to_move).exists():
            shutil.move(path / file_to_move, path / new_dir / file_to_move)
        else: print('File does not exist')
    elif ch == 6: 
        file_to_copy = input('Enter file name to copy: ')
        if (path / new_dir / file_to_copy).exists():
            shutil.copy(path / new_dir / file_to_copy, path / file_to_copy)
        else: print('File does not exist')