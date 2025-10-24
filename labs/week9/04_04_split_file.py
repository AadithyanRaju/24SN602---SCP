"""

1. Open winnie_pooh.txt
2. read in 100 lines at a time
3. after each 100 lines, write those lines to a new file
4. name each file differently (create a system to auto-increment the file names)
5. place all the files in a new folder (that you needed to create earlier)


"""

import os
from pathlib import Path


new_dir = Path('pooh_splits')
new_dir.mkdir(exist_ok=True)

with open('/home/aadithyan/github/24SN602---SCP/labs/week9/winnie_pooh.txt', 'r') as infile:
    lines = infile.readlines()
    chunk_size = 100
    total_lines = len(lines)
    num_files = (total_lines + chunk_size - 1) // chunk_size  
    for i in range(num_files):
        chunk = lines[i*chunk_size:(i+1)*chunk_size]
        out_path = new_dir / f'pooh_part_{i+1}.txt'
        with open(out_path, 'w') as outfile:
            outfile.writelines(chunk)
        print(f'Created file: {out_path} with {len(chunk)} lines')