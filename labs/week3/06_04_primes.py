# Exercise

# Write a python program to print all prime numbers between 0 to 100 , and print how many prime numbers are there
# if you don't know an algorithm to check for primes
# ask Dr. Kurunandan Sir
# google it

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

for i in range(2,101):
    if is_prime(i):
        print(i, end = " ")
        