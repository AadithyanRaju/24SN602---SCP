# write code to generate a dictionary where
# each key is:an integer divisible by 3
# each value is: a list containing the even numbers in the range of key

# Take all the numbers divisible by 3 from 1-301
# example output
# {3: [2], 6: [2,4,6], 9:[2,4,6,8].... 300:[2,4,6,...288]}

print({x:[y for y in range(2,x,2)] for x in range(3, 301, 3)})