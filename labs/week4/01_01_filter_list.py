# Exercise

# stage 1
# Write a program to count the number of strings where the string length is 2 or more
# sample list: ['aaaa', 'a', 'ab', 'abc', ]
# result : 3
sample_list = ['aaaa', 'a', 'ab', 'abc']
print(f"Number of strings with length 2 or more: {len([x for x in sample_list if len(x)>2])}")

## Stage 2
# Now count the number of strings that have length 2 or more
# AND the first and last character are same from a given list of strings.

# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
sample_list = ['abc', 'xyz', 'aba', '1221']
print(f'Result: {len([x for x in sample_list if x[0]==x[-1]])}')