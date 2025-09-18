"""
Write a function that accepps the following arguments
INPUT:
    name: str
    job : str
    * args: adjectives (str) that describe things (i.e "happy", " sad")
    **args: possessions (str): value (int / float)
Output:
   Form a  nice string that explains everything relevant



example input:
   ('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20)
output:
   "Gilad is a teacher who is happy, amazing, and sooooo cool. Gilad has a bike worth 2000, a house worth 1000, and shoes with 20"


The string should accomadate any number of *args and **kwargs.
"""

def fun1(name, job, *args) -> str:
    result = f"{name} is a {job} who is "
    l = len(args)
    if l >1:
      result += ""
      for i in args[:-1]:
        result += f"{i}, "
      result += f"and {args[-1]}"
    elif l == 1:
       result += f"{args[-1]}"
    else:
       result += "nothing"
    return result


def fun2(name, job, *args, **kwargs):
   result = fun1(name, job, *args) + "."
   result2 = f" {name} has"
   if kwargs:
      for key, value in kwargs.items():
         result2 += f" a {key} worth {value},"
      result2 = result2[:-1] + "."
      commaCount = result2.count(",")
      if commaCount>=1:
         i = -1
         while result2[i]!= ',':
            i-=1
         result2 = result2[:i] + " and" + result2[i+1:]
      return result + result2
   return result

print(fun2('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20))
