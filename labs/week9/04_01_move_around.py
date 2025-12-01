"""
Use the following commands to look around your directory
You may want to do this exercise interactively with an interpreter session

Path.cwd() gets the current working directory, returns a Path object
os.chdir(path)  changes directory	

os.listdir() files and directories, returns a list
Path.glob(“*”)  returns a generator that you can use to iterate over all files and directories. Advantage is you can filter the results easily on the input.
Path.iterdir()

"""

from pathlib import Path
import os
path = Path.cwd()
while True:
    print('''
        -----MENU-----
        1. Print Working Directory
        2. List Working Directory
        3. Change Working Directory
        4. Exit
        --------------
        ''')
    ch = int(input('Enter Choice: '))
    if ch == 4: break
    elif ch == 1: print(path)
    elif ch == 2: print(os.listdir(path))
    elif ch == 3 :
        newpath = input()
        if newpath in os.listdir() : path /= newpath
        elif newpath[0] == '/' : 
            os.chdir(newpath)
            path = os.path
