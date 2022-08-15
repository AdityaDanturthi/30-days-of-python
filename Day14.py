# Higher order functions

# Function as a parameter
def addnums(nums): # regular function
    return sum(nums) # in-built sum function

def higherorderfunction(f, lst): # function as a parameter
    total = f(lst)
    return total

result = higherorderfunction(addnums, [1, 2, 3, 4, 5])
print(result)

# Function as a return value
def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def absolute(x):
    if x >= 0:
        return x
    else:
        return -(x)
    
def hof(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
res = hof('square')
print(res(2))

res = hof('cube')
print(res(2))

res = hof('absolute')
print(res(-2))

# Python closure: nested functions

def add10():
    ten = 10
    def add(num):
        return num + ten
    return add

nestedfunc = add10()
print(nestedfunc(2))
print(nestedfunc(5))

# Python Decorators

# Normal function
def greeting():
    return 'Hi'

def uppercasedec(function):
    def wrapper():
        func = function()
        touppercase = func.upper()
        return touppercase
    return wrapper
g = uppercasedec(greeting)
print(g())

# Converting normal function into a decorator

def uppercasedeco(function):
    def wrapper1():
        func1 = function()
        touppercase1 = func1.upper()
        return touppercase1
    return wrapper1

@uppercasedeco
def greeting1():
    return 'Hi, how are you?'
print(greeting1())


# Applying multiple decorators to a single function

#First decorator
def uppercasedecorator(function):
    def wrapper2():
        func = function
        uppercasefunctionvar = func.upper()
        return uppercasefunctionvar
    return wrapper2

def splitstringdecorator(function):
    def wrapper2():
        func = function
        splitstringfuncvar = func.split()
        return splitstringfuncvar
    return wrapper2

@uppercasedecorator
@splitstringdecorator
def greeting2():
    return 'Hey!'
print(greeting2)

# Accepting parameters in decorator functions
def decoratorwithparameters(function):
    def wrapperacceptingparameters(para1, para2, para3):
        function(para1, para2, para3)
        print('I live in {}.'.format(para3))
    return wrapperacceptingparameters

@decoratorwithparameters
def details(firstname, lastname, country):
    print('I am {} {}! I live in {}.'.format(firstname, lastname, country))

details('Aditya', 'Danturthi', 'Canada')

# Built-in higher order functions

# Map function

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def square(x):
    return x ** 2
squarednums = map(square, numbers)
print(list(squarednums))

# Example 1: Appying a lambda function
squarednums1 = map(lambda x: x** 2, numbers)
print(list(squarednums1))

# Example 2: converting string list to int
numstr = ['1', '2', '3', '4', '5']
numint = map(int, numstr)
print(list(numint))

# Example 3: Upper case
names = ['Aditya', 'Alex']
def changetoupper(name):
    return name.upper()

uppercasednames = map(changetoupper, names)
print(list(uppercasednames))

# Example 3 with lambda function
uppercasednames1 = map(lambda name: name.upper(), names)
print(list(uppercasednames1))

# Filter function

# Example 1
allnums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even(num):
    if num % 2 == 0:
        return True
    return False

evennums = filter(even, allnums)
print(list(evennums))

# Example 2
allnums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def odd(num):
    if num % 2 != 0:
        return True
    return False

oddnums = filter(odd, allnums)
print(list(oddnums))

# Example 3: Filter strings longer than 7 characters
strlist = ['aaaaaaaaaaaa', 'bbb', 'ccccccccccccc', 'ddddddd', 'eeeeeeeeee']
def checkstr(check):
    if len(check) > 7:
        return True
    return False
longstrs = filter(checkstr, strlist)
print(list(longstrs))

# Reduce function
from functools import *
numstr = ['1', '2', '3', '4', '5']
def addnums(x, y):
    return int(x) + int(y)

total = reduce(addnums, numstr)
print(total)

numstr = ['1', '2', '3', '4', '5']
def addstrs(x, y):
    return x + y

allstrs = reduce(addstrs, numstr)
print(allstrs)