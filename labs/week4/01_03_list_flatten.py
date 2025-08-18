#Exercise

# Write a Python program to flatten a shallow list

#Sample Input: [[2,4,3],[1,5,6], [9], [7,9,0]]
#Output: [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

sample_list =  [[2,4,3],[1,5,6], [9], [7,9,0]]
output_list = []
for i in sample_list:
    output_list+=[*i]
print(output_list)
