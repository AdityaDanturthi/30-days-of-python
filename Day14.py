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
        touppercase =func.upper()
        return touppercase
    return wrapper
g = uppercasedec(greeting)
print(g())

# Converting normal function into a decorator

def uppercasedeco(function):
    def wrapper1():
        func1 = function
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