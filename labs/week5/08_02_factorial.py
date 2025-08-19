# write a recursive function to calculate the factorial


def factorial(n):
    """
    input: 
        n: int
    returns: 
        factorial of n
    
    reminder: factorial 8! is
    8*7*6*5*4*3*2*1
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(f"factorial(5) = {factorial(5)}")  
