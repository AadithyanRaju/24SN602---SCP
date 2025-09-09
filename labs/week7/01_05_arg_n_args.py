# write a function that takes two positional arguments and uses *args
# your function should:
"""
arguments:
    name: name of person
    job: job title of person
    *args: possesions that they own

returns --> Str
   It should return a string that says a nice message like
  "hello Gilad, I heard your job of washing dishes allows you to own a lawn-mower, house, cat, and bat"

Remember, your string needs to _grow_ with the *args - it needs infinite potential!

"""

def fun(name, job, *args) -> str:
    result = f"hello {name}, I heard your job of {job} allows you to own "
    l = len(args)
    if l >1:
      result += "a "
      for i in args[:-1]:
        result += f"{i}, "
      result += f"and {args[-1]}"
    elif l == 1:
       result += f"a {args[-1]}"
    else:
       result += "nothing"
    return result

print(fun('a','b','c','d','e'))
print(fun('a','b','c'))
print(fun('a','b'))
       
    