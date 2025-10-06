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
   if args:
      adjectives = ", ".join(args[:-1])
      if adjectives:
         adjectives += f", and {args[-1]}"
      else:
         adjectives = args[0]
      return f"{name} is a {job} who is {adjectives}"
   else:
      return f"{name} is a {job} who is nothing"

def fun2(name, job, *args, **kwargs):
   result = fun1(name, job, *args) + "."
   if kwargs:
      possessions = [f"{key} worth {value}" for key, value in kwargs.items()]
      if len(possessions) > 1:
         possessions_str = ", ".join(possessions[:-1]) + f", and {possessions[-1]}"
      else:
         possessions_str = possessions[0]
      result += f" {name} has {possessions_str}."
   return result

print(fun2('Gilad', 'teacher', 'happy', 'amazing', 'sooooo cool', bike = 2000, house = 1000, shoes = 20))
