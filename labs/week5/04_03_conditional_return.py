# write a function that has more than one return statement


def greater_than_x(n, x):
    """
    input:
       n: int
       x: int
    returns:
       True if n > x
       False otherwise
    """
    return n>x

print(greater_than_x(5, 3))  
print(greater_than_x(2, 4))  

### Extra credit
# Is it required to use the else block? Can you write the above code with only the if statement but no else?
#no
