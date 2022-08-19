# Exception handling
from datetime import datetime

try:
    print(10 + '2')
except:
    print(' Something went wrong')

# Kind of error
try:
    name = input('Please input your name: ')
    birthyear = int(input('Please input your birth year: '))
    dateobj = datetime.now()
    thisyear = dateobj.year
    thisyear = int(thisyear)
    age = thisyear - birthyear
    print(f'Hi {name}! You are {age} years old.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# Shortening the above code
try:
    name = input('Please input your name: ')
    birthyear = int(input('Please input your birth year: '))
    dateobj = datetime.now()
    thisyear = dateobj.year
    thisyear = int(thisyear)
    age = thisyear - birthyear
    print(f'Hi {name}! You are {age} years old.')
except Exception as e:
    print(e)

# Packing and unpacking arguments in python
# We use two operators:

# * for tuples
# ** for dictionaries

# Unpacking a list
def sumofnums(a,b,c,d):
    return a+b+c+d

lst = [1,2,3,4]
# print(sumofnums(lst)) #Error: This function takes numbers (not a list) as arguments. Let us unpack/destructure the list.
print(sumofnums(*lst))

# Unpacking can be used in built-in functions
randomlst = range(0,10)
print('List of numbers using range: ',list(randomlst))

args = [0,9]
randomlist1 = range(*args)
print('List of numbers using unpacking in range: ',list(randomlist1))

# A list or tuple can also be unpacked like this:
countries = ['US', 'Canada', 'Switzerland']
us, *rest= countries
print(us, rest)

one, *restnums= lst
print(one, restnums)

# Unpacking a dictionary
def unpackingdetails(name, country, age):
    return f'{name} lives in {country}. He is {age} years old'

dct = { 'name': 'Aditya', 'country': 'Canada', 'age': 260}
print(unpackingdetails(**dct))

# Packing: For accepting unlimited number of arguments

# Packing a list
def sumnums(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sumnums(1,2,3,4,5))
print(sumnums(1,2,3,4,5,6,7,8,9,10))

# Packing a dictionary

def packingdetails(**kwargs):
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')
    return kwargs

print(packingdetails(name = 'Aditya', country = 'Canada', age = 260))

# Spreading
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]

lst = [ 0,*lst1,*lst2,9,10]
print(lst)

northamericancountries = ['USA', 'Canada']
asiancountries = ['Japan', 'India', 'China']
countrieslst = [*northamericancountries,*asiancountries]
print(countrieslst)

# Enumerate
for index, item in enumerate([10,20,30]):
    print(index,item)


for index, i in enumerate(countrieslst):
    print('Hello')
    if i == 'Japan':
        print(f'The country {i} has been found at {index}')