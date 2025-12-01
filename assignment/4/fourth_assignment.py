from pathlib import Path

"""                                                                                                                     
#1
9 marks
Write a function that accepts a single list of strings it should filter it.
You should return 3 separate lists, each one of which contains a certain category of strings 
Categories:
    number_only_list : the string contains only digits like: "123"
    letter_only_list : the string contains only letters like: "abc"
    full_mix_list : the string contains anything like: "https://my_website.com/%00/etc/passwd" (this includes spaces and symbols)

You need to return all three lists in a tuple with the follow order:
(number_only_list, letter_only_list, full_mix_list)
In each sublist the elements should be in the same order of appereance as in the initial list.

example input: ["123","1asd23","manzanas","128753","other language","ajsh.saso"]
example output: (['123', '128753'], ['manzanas'], ['1asd23', 'other language', 'ajsh.saso'])

example input: ["123","6","3038"]
example output: (['123', '6', '3038'], [], [])

Note: the space character " " counts as something else than letter, so it should go in the full_mix_list
If a type of string is missing from the input (i.e: no strings with numbers only are found) you should return an empty list for that type
"""

def sort_by_component(inputList: list[str]) -> tuple[list[str], list[str], list[str]]:
    number_only_list, letter_only_list, full_mix_list = [],[],[]
    for value in inputList:
        if value.isnumeric():number_only_list.append(value)
        elif value.isalpha():letter_only_list.append(value)
        else:full_mix_list.append(value)
    return (number_only_list, letter_only_list, full_mix_list)

print(sort_by_component(["123","1asd23","manzanas","128753","other language","ajsh.saso"]))

"""
#2
9 marks
Write a function that accepts an infinite amount of positional arguments
All the inputs will be integers.
Your function should take all the arguments and place them into tuples of 
4 elements each. 
Each tuple will have the following structure:
(first_element,"and",second_element,first_element+second_element)
Put all the tuples in a list, return the list.

In case you receive an odd amount of arguments, fill the last sum with 0 
(the number zero)

Input: Integers
Output: List of Tuples

example input:  infinite_sums(1,2,3,4,5,6,7,8)
example output: [(1, 'and', 2, 3), (3, 'and', 4, 7), (5, 'and', 6, 11), (7, 'and', 8, 15)]

example input:  infinite_sums(33, -30, 21, 15, 35, 58, -31)
example output: [(33, 'and', -30, 3), (21, 'and', 15, 36), (35, 'and', 58, 93), (-31, 'and', 0, -31)]
"""

def infinite_sums(*values: int):
    result = []
    len_values = len(values)
    for i in range(0, len_values, 2):
        second_element = 0 if i + 1 >= len_values else values[i + 1]
        result.append((values[i], "and", second_element, values[i] + second_element))
    return result

"""
#3
9 marks
Write a function that "encrypts" a string with the following rules

    - Every letter is mapped to a number, based on it's position in the alphabet
    So a-->1, b-->2, c-->3.... x-->24, y-->25 z-->26  
    (This rule applies for upper and lower case)

Your function should return a text encrypted in this way

Input1: String
Output: String

example input: "abc"
example output: "123"

example input: "this is a sentence longer"
example output: "208919 919 1 195142051435 1215147518"

"""

def encrypt(inputString:str): 
    return "".join([str((ord(y)-64) if y.isalpha() else y )for y in inputString.upper()])
"""
#4
9 marks
Complete the folder_description function that creates a dictionary mapping each datatype to the amount
of files present in that folder. 
Your function will receive one input: folder_name
It will return a dictionary in which the key represents the file type (".doc",".pptx",".docx",".pdf",".txt", etc....)
and the value represents how many files of each type is present in that folder. Your dictionary should only map to the present extensions in that folder
(if there is no pdf files, it should not have a key for ".pdf")

Input: String
Output: Dictionary

EXAMPLES:
input_A : folder_description("my_desktop")
output_A : {'.pdf': 3, '.jpg': 2, '.csv': 2, '.png': 1}

input_B : folder_description("video_dic")
output_B: {'.jpg': 4, '.pdf': 6, '.csv': 4, '.png': 2}

"""

def folder_description(dir:str):
    import collections, os
    return dict(collections.Counter(['.'+x.split('.')[-1] for x in os.listdir(dir)]))

"""
#5
9 marks
Make a function that will inspect a folder and will return all the file names of a specific type. 
Your function will receive two inputs: folder_name and file_type
It will return a set of strings. Each string will be the name of the file (including the extension)

Input: String , String
Output: Set of Strings

EXAMPLES:

input_A : folder_inspector("my_desktop",".pdf")
output_A : {'shoping_list.pdf', 'test.pdf', 'travels.pdf'}

input_B : folder_inspector("my_desktop",".csv")
output_B: {'SampleCSVFile_2kb.csv', 'SampleCSVFile_11kb.csv'}

"""

def folder_inspector(dir,suffex):
    import os
    return set([x for x in os.listdir(dir) if x.split('.')[-1] == suffex[1:]])