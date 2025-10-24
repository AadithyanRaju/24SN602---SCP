"""
#1
8 marks

Complete the most_repeated_word function to find the word that appears most frequently in a string.
The function should receive 1 input: a string.

It will return a dictionary with the key being the most repeated word and the value being the number of times it appears.
If there are multiple words with the same maximum count, return the one that appears first in the string.

Input: String
Output: Dictionary

Example input: "the student studied hard for the exam and the student passed with excellent grades"
Example output: {'the': 3}

Example input: "python is a great programming language and python is used in many applications"
Example output: {'python': 2}

Example input: "weather today is sunny and the weather forecast shows more sunny days ahead"
Example output: {'weather': 2}
"""


def most_repeated_word(inStr:str):
    resultDict = dict()
    for i in inStr.split():
        if i in resultDict.keys():resultDict[i]+=1
        else:resultDict[i]=1
    maxWord = inStr.split()[0]
    for i in resultDict.keys():
        if resultDict[i]>resultDict[maxWord]:maxWord = i
    return {maxWord:resultDict[maxWord]}


"""
#2
7 marks

Complete the function average_finder that will receive a list of numbers in string format, 
and will calculate the average of all numbers. After that will return a dictionary with 
the keys "average" and "count", where "average" contains the calculated average as a float 
rounded to 2 decimal places, and "count" contains the total number of elements as an integer.

Input: List
Output: Dictionary

example input: ['15', '25', '35', '45', '55']
example output: {'average': 35.0, 'count': 5}

example input: ['10', '20', '30', '40', '50', '60']
example output: {'average': 35.0, 'count': 6}
"""

def average_finder(inList:list):
    avg, count = 0,0
    for i in inList: avg, count = avg + int(i), count + 1
    avg/=count
    return {'average': avg, 'count': count}
"""
#3
8 marks 

Complete the temperature_classifier function that accepts a tuple of values that represent temperature measurements in Celsius.

When the temperature is equal to or above 30°C, it is considered: "Hot"
When the temperature is between 20-29°C, it is considered: "Warm"
When the temperature is between 10-19°C, it is considered: "Cool"
When the temperature is equal to or below 9°C, it is considered: "Cold"

Your function should make a summary of the given values in a dictionary, 
using the exact keys: "Hot", "Warm", "Cool" and "Cold".

Input: Tuple of Integers
Output: Dictionary

example input: temperature_classifier(35, 25, 5, 15, 12, 28, 18, 22, 8, 2, 26, 4, 24, 32, 40)
example output: {'Hot': 3, 'Warm': 4, 'Cool': 4, 'Cold': 4}

example input: temperature_classifier(2, 8, 4, 16, 25, 18, 28, 22, 14, 1, 26, 24, 0, 20, 30, 34, 32, 19, 17, 3)
example output: {'Hot': 2, 'Warm': 6, 'Cool': 6, 'Cold': 6}
"""

def temperature_classifier(inTuple):
    result = {'Hot': 0, 'Warm': 0, 'Cool': 0, 'Cold': 0}
    for i in inTuple:
        if i >= 30 : result['Hot']+=1
        elif i >= 20 : result['Warm']+=1
        elif i >= 10 : result['Cool']+=1
        else: result['Cold']+=1
    return result 


"""
#4
8 marks

Complete the vowel_cipher function that creates a simple cipher by substituting vowels with different numbers of asterisks.
The function should receive 1 input: a string.

It will return a new string where vowels are replaced with asterisks as follows:
- 'a' or 'A' → 1 asterisk (*)
- 'e' or 'E' → 2 asterisks (**)
- 'i' or 'I' → 3 asterisks (***)
- 'o' or 'O' → 4 asterisks (****)
- 'u' or 'U' → 5 asterisks (*****)

All other characters (consonants, numbers, spaces, punctuation) remain unchanged.

Input: String
Output: String

example input: "Hello World"
example output: "H**ll**** W****rld"

example input: "Programming is fun"
example output: "Pr****gr*mm***ng ***s f*****n"

example input: "The quick brown fox"
example output: "Th** q********ck br****wn f****x"
"""

def vowel_cipher(inStr:str):
    result,vovels = '','aeiou'
    for i in inStr:result += ('*'*(vovels.find(i)+1) if (i.lower() in vovels) else i)
    return result

"""
#5
9 marks

Write a function `email_validator` to check the validity of an email address. 
Return the boolean: True if valid, False otherwise
  
Validation : 
Only letters of the english alphabet (uppers and lowers), digits, and the symbols in the list [., -, _] are allowed in the local part.

It must have:
    - At least 1 letter between [a-z] and 1 letter between [A-Z] in the local part. 
    - At least 1 digit from [0-9] in the local part. 
    - At least 1 character from [., -, _] in the local part.
    - Only these special characters are allowed [., -, _] in the local part, anything else is not allowed.
    - Must contain exactly one @ symbol.
    - Must have a valid domain part (at least one letter after @).
    - Minimum length 8 characters for the entire email. 
    - Maximum length 25 characters for the entire email. 

Input: String
Output: Boolean

Examples:
Input: "User123@domain.com"
Output: False

Input: "AbC1234.@test.org"
Output: True

Input: "test@domain"
Output: False

hint:
Search about the string functions: .isupper(), islower(), isdigit(), .split()
"""

def email_validator(email:str):
    lenEmail = len(email)
    if lenEmail < 8 or lenEmail > 25 : return False
    parts = email.split('@')
    if len(parts) != 2 : return False
    localPart = parts[0]
    ul, ll , d, c = 0,0,0,0
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    digits = '1234567890'
    symbols = '.-_'
    for i in localPart:
        if i in letters : ll+=1
        elif i in letters.upper() : ul+=1
        elif i in digits: d += 1
        elif i in symbols: c +=1
        else: return False
    if (ul == 0 or ll == 0 or d == 0 or c == 0): return False
    if len(parts[1]) == 0: return False
    return True

