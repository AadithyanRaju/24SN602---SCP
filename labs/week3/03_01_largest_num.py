# Exercise

num_one = 10
num_two = 2
num_three = 1010
num_four = 123

# Use if / else statement to find the largest number.

if num_one >= num_two and num_one >= num_three and num_one >= num_four:
    print(f"The largest number is: {num_one}")
elif num_two >= num_one and num_two >= num_three and num_two >= num_four:
    print(f"The largest number is: {num_two}") 
elif num_three >= num_one and num_three >= num_two and num_three >= num_four:
    print(f"The largest number is: {num_three}")
else:
    print(f"The largest number is: {num_four}")