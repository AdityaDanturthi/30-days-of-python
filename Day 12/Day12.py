# Modules: A module is a file containing a set of codes or a set of functions which can be included in an application. A module could be a file containing a single variable, a function or a big code base.

# Creating a module: fullnamefirstmodule.py
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
from random import random, randint

print(random())
print(randint(0,10))
