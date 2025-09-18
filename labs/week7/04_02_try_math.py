""""
import the math library and use it to automatically generate a random list of numbers
You should generate 1000 random numbers.


"""
import math
import time

def pseudo_random(seed=None):
    if seed is None:
        seed = int(time.time() * 1000) & 0xFFFFFFFF
    a = 1664525
    c = 1013904223
    m = 2**32
    while True:
        seed = (a * seed + c) % m
        yield seed / m  

gen = pseudo_random()
random_numbers = [math.floor(next(gen) * 100) for _ in range(1000)]
print(random_numbers)


