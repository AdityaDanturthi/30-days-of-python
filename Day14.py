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

