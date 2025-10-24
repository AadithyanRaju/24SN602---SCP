"""

Create two new folders
a. vowel
b. consonant

Iterate over your previously created files from 04_04_split_file.py
Open each file and check if the first word begins in a vowel or consonant
If it begins in a vowel, move the file to the vowel folder
Otherwise move the file to the consonant folder

"""

from pathlib import Path
import shutil
import os

source_dir = Path('/home/aadithyan/github/24SN602---SCP/pooh_splits')
vowel_dir = Path('/home/aadithyan/github/24SN602---SCP/labs/week9/vowel')
consonant_dir = Path('/home/aadithyan/github/24SN602---SCP/labs/week9/consonant')

vowel_dir.mkdir(exist_ok=True)
consonant_dir.mkdir(exist_ok=True)

for file in source_dir.iterdir():
    if file.is_file():
        with open(file, 'r') as f:
            l = f.readline()
            while not l:
                l=f.readline()
            first_word = l
            if first_word[0].lower() in 'aeiou':
                shutil.move(str(file), str(vowel_dir / file.name))
            else:
                shutil.move(str(file), str(consonant_dir / file.name))