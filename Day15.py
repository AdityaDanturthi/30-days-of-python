# Type of errors

# SyntaxError
print 'Hello world' # SyntaxError: missing parantheses

# NameError
print(a) # NameError: a is not defined

# IndexError
nums = [1, 2, 3, 4, 5]
print(nums[5]) # IndexError: list index out of range

# ModuleNotFoundError
import maths # ModuleNotFoundError: No module named 'maths'

# AttributeError
import math
math.PI # AttributeError: module math has no attribut 'PI'

# KeyError
details = {'name': 'Aditya', 'age': 260}
details['name']
details['country'] # KeyError: 'country'

# TypeError
1 + '2' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ImportError
from math import power # ImportError: cannot import name 'power' from 'math'

# ValueError
int('12a') # ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError
1/0 # ZeroDivisionError: division by zero



