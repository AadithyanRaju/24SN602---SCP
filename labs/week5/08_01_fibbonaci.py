# wrtie a recursive fibonacci function


def fib(n):
    """
    input: 
        n: int

    return:
        fibbonacci number for n
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


# fib(6) should return 8
# fib(10) should return 55

print(f"fib(6) = {fib(6)}")
print(f"fib(10) = {fib(10)}")