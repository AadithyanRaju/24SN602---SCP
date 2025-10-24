"""
use a context manager to open the file winnie_pooh.txt

try it two ways
a) make a Path object that points to winnie_pooh.txt
b) just write it in as a string (don't use a Path object)

Both are valid! The first method is the OO way and will yield better programs down the line.
The second way is fine for quick scripts though

## Tasks to try
1. Print out of the first line of the file
2. Print out all the entire file
3. Print in the last line of the file
4. Add a new sentence to the file "I AM A NEW SENTENCE!"
5. 

"""
from pathlib import Path

pathObj = Path.cwd() / "labs" / "week9" / "winnie_pooh.txt"
path = '/home/aadithyan/github/24SN602---SCP/labs/week9/winnie_pooh.txt'

f = open(path, 'r')
print(f"first line = {f.readline()}")
f.close()

f = open(path, 'r')
print('Full')
for line in f.readlines():
    print(line)
f.close()


f = open(path, 'r')
print('Last')
print(f.readlines()[-1])
f.close()

f = open(path, 'a')
f.write('I AM A NEW SENTENCE!')
f.flush()
f.close()
