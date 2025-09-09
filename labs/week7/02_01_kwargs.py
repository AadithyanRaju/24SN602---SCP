## write a function that uses **kwargs as input
## it should print out the sum of all the integers found in the values

"""
input: hi = 2020, bye = 1000, see = 2, def = 'this'
output : 3022

The function should work for any kind of values and as many keyword arguments as the use would like to pass

"""
from random import choice
def fun(**kwargs):
    result = 0
    for name, value in kwargs.items():
        if type(value) == int:
            result += value
    return result

print(fun(hi = 2020, bye = 1000, see = 2, def1 = 'this'))
