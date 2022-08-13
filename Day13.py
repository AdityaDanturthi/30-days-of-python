# List comprehension
# syntax: [i for i in iterable if expression]

# Ways to convert a string to a list of characters
from random import random


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