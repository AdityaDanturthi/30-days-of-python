# List comprehension
# syntax: [i for i in iterable if expression]

# Ways to convert a string to a list of characters
from random import random
from stringprep import c22_specials


language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst1 = [i for i in language]
print(type(lst1))
print(lst1)

# Generating a list of numbers
numlst = [i for i in range(11)]
print(type(numlst))
print(numlst)

# Perofrming mathematical operations while creating a list using list comprehension
squareslst = [i*i for i in range(11)]
print(type(squareslst))
print(squareslst)

# Making a list of tuples
numtuple = [ (i, i*i) for i in range(11)]
print(type(numtuple))
print(numtuple)

# List comprehension combined with if statement

# Even numbers list
evennums = [i for i in range(11) if i % 2 == 0]
print(type(evennums))
print(evennums)

# Odd numbers list
oddnums = [i for i in range(11) if i % 2 != 0]
print(type(oddnums))
print(oddnums)

# Filter positive and even numbers from randomnumlst
randomnumlst = [-8 -7, -3, -1, 0, 1, 3, 4, 5, 6, 8, 10]
posevennumlst = [ i for i in randomnumlst if i > 0 and i % 2 == 0]
print(type(posevennumlst))
print(posevennumlst)

# Falttening a three dimensional array
multiplelsts = [[1,2,3], [4,5,6], [7,8,9]]
convertedsinglelst = [ num for row in multiplelsts for num in row]
print(type(convertedsinglelst))
print(convertedsinglelst)

# Regular function
def addnums(a,b):
    return a + b
print(addnums(1,2))
# regular function converted into a lambda function

total = lambda a1,b1 : a1 + b1
print(total(2,3))

# Self-invoking lambda function
print((lambda a, b: a - b)(5,3))

squares = lambda x: x*x
print(squares(5))

# Multiple variables
multiplenums = lambda a2, b2, c2: a2+ b2+ c2
print(multiplenums(2,3,4))

# Lambda function inside another function
def exponential(d):
    return lambda n: d ** n

print(exponential(2)(2))

# Exercises: Day 13

# Filter only negative and zero in the list using list comprehension: numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
newlist = [x for x in numbers if x <= 0]
print(newlist)

"""Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

output
[1, 2, 3, 4, 5, 6, 7, 8, 9]"""

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flattenedlst =  [x for row in list_of_lists for x in row]
print(flattenedlst)

"""Flatten the following list to a new list:
output:
[['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]"""

countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]

flattenedcountrieslst = [country for row in countries for country in row]
print(flattenedcountrieslst)
