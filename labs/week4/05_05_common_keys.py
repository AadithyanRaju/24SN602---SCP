# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4, "d": 2}

dict_3 = {}
for i in dict_1.keys():
    if i in dict_2.keys():
        dict_3[i] = dict_1[i] + dict_2[i]
    else:
        dict_3[i] = dict_1[i]
for i in dict_2.keys():
    if i not in dict_3.keys():
        dict_3[i] = dict_2[i]
print(dict_3)