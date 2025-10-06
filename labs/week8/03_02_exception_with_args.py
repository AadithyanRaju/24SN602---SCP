"""
rewrite inner_multiple from  Week 8

# write a function accepts as input an infinite amount of tuples
# it returns a list, where each element is the inner multiplication

# example input: (1,2), (2,2), (3,2), (4,5)
# output: [2,4,6,20]


Iterate over the args summing them up. 
Use an if statement ot check if the user passed tuples.
Raise an exception if they passed something else
"""

def fun(*args:tuple) -> list:
    result = []
    for i in args:
        if isinstance(i, tuple) and len(i) == 2:result+=[i[0]*i[1]]
        else:raise Exception("Tuple must have exactly two elements")
    return result
