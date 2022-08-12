# Modules: A module is a file containing a set of codes or a set of functions which can be included in an application. A module could be a file containing a single variable, a function or a big code base.

# Creating a module: fullnamefirstmodule.py
import fullnamefirstmodule 
print(fullnamefirstmodule.fullname('Aditya', 'Danturthi'))
print(fullnamefirstmodule.addtwonumbers(1,2,3,4,5,6,7,8,9,10))

# Importing in-built modules
import os

# Creating a directory
os.mkdir('Directory name')

# Changing the path of the current directory
os.chdir('path')

# Getting the current working directory
os.getcwd()

# Removing a directory
os.rmdir()

# Sys module
import sys

print('Computer: Hi {}!\n Computer: How are you?\n Aditya: {}! \n Computer: That\'s good!'.format(sys.argv[1], sys.argv[2]))

sys.exit()
sys.maxsize # largest integer that will be accepted

sys.path # environment path
sys.version # return version of python

# Statistics module
import statistics