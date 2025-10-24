"""
Let's make a very basic Path object

"""

from pathlib import Path

##
cwd = Path.cwd()

## create a new path using concatenation

# or you can use the special / symbol (overloaded for concatenation)
new_path = cwd / "labs" 
# you can use cwd.joinpath
new_path = new_path.joinpath("week9", "02_01_basic_path.py")
## examine your new path object
print(f"new_path = {new_path}")
## print the following parts
# .parent
print(f"new_path.parent = {new_path.parent}")
# .anchor
print(f"new_path.anchor = {new_path.anchor}")
# .name
print(f"new_path.name = {new_path.name}")
# .stem
print(f'new_path.stem = {new_path.stem}')
# .suffix
print(f'new_path.suffix = {new_path.suffix}')


## check if your path is a directory or file

## .is_file()
print(f'new_path.is_file() = {new_path.is_file()}')

## .is_dir()
print(f'new_path.is_dir() = {new_path.is_dir()}')

## print out your path and look at the type (you may need to print(type(your_path_here)))
print(new_path)
print(type(new_path))
## does it accurately reflect your OS?
