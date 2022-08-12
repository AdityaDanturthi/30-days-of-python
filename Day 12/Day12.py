# Modules: A module is a file containing a set of codes or a set of functions which can be included in an application. A module could be a file containing a single variable, a function or a big code base.

# Creating a module: fullnamefirstmodule.py
from asyncio.windows_events import NULL
from fullnamefirstmodule import *
print(fullname('Aditya', 'Danturthi'))
print(addtwonumbers(1,2,3,4,5,6,7,8,9,10))

# Importing in-built modules
import os

# Creating a directory
#os.mkdir('Directory name')

# Changing the path of the current directory
#os.chdir('path')

# Getting the current working directory
# os.getcwd()

# Removing a directory
#os.rmdir()

# Sys module
# import sys

# print('Computer: Hi {}!\n Computer: How are you?\n Aditya: {}! \n Computer: That\'s good!'.format(sys.argv[1], sys.argv[2]))

# sys.exit()
# sys.maxsize # largest integer that will be accepted

# sys.path # environment path
# sys.version # return version of python

# Statistics module
from statistics import *

ages = [21,22,23,24,25,26,27,26,26,25,24,22,21]
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

# Math module
import math

print(math.pi)
print(math.sqrt(4))
print(math.pow(2,3))
print(math.floor(9.81))
print(math.ceil(9.81))


from math import *

print(pi)
print(sqrt(4))
print(pow(2,3))
print(floor(9.81))
print(ceil(9.81))

from math import pi as PI
print(PI)

# String module
import string
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# Random module
from random import *

print(random())
print(randint(0,10))

# def userid():
#     useridstring = ''
#     for i in randrange(0,9):
#         if len(useridstring) == 6:
#             break
#         j = str(i)
#         useridstring += j
#         # if j == '1':
#         #     useridstring += 'ee'
#         # continue 
#     return useridstring
# print(userid())


# Day 12: Exercise 1
# def userid():
#     useridstring = ''
#     while len(useridstring) < 6:
#         randomnumber = randint(0,9)
#         randomletter = choice(string.ascii_letters)
#         randomnumber = str(randomnumber)
#         randomstring  = randomnumber + randomletter
#         useridstring += randomstring 
#     return useridstring

# print(userid())
# Day 12: Exercise 2
# def userid(numberofchars,numberofstringsreq):
#     useridstring = ''
#     useridstringlist = []
#     i = 0
#     while i < numberofstringsreq:
#         while len(useridstring) < numberofchars:
#             randomnumber = randint(0,9)
#             randomletter = choice(string.ascii_letters)
#             randomnumber = str(randomnumber)
#             randomstring  = randomnumber + randomletter
#             useridstring += randomstring 
#         useridstringlist.append(useridstring)
#         i += 1
#     return useridstringlist

# numberofchars = int(input('Number of characters required:'))
# numberofstringsreq = int(input('Number of strings required:'))
# print(userid(numberofchars,numberofstringsreq))

# Day 12: Exercise 1
def userid(numberofchars):
    useridstring = ''
    useridstringlist = []
    while len(useridstring) < numberofchars:
        randomnumber = randint(0,9)
        randomletter = choice(string.ascii_letters)
        randomnumber = str(randomnumber)
        randomstring = choice(randomnumber+randomletter)
        useridstring += randomstring 
    useridstringlist.append(useridstring)
    return useridstringlist

numberofchars = int(input('Number of characters required:'))
# numberofstringsreq = int(input('Number of strings required:'))
print(userid(numberofchars))