# Statistical Analysis

# Numpy
from random import randint
import numpy as np
print('numpy version: ', np.__version__)
print(dir(np)) # prints available functions

# Creating a python list
pylist  = [1,2,3,4,5]

print('Type: ',type(pylist))
print(pylist)

twodimlst = [[1,2],[3,4],[5,6],[7,8],[9,10]]
print('Two dimensional list: ', twodimlst)

# Creating a numpy array from python list
nparray = np.array(pylist)
print('Type: ', type(nparray))
print(nparray)

# Creating a float numpy array
nparrayfloat = np.array(pylist, dtype = float)
print('Type: ', type(nparrayfloat))
print(nparrayfloat)

# Creating boolean numpy array from a list
listforbool = [0,1,1,0,1,0, -1]
nparraybool = np.array(listforbool, dtype= bool)
print('Type: ', type(nparraybool))
print(nparraybool)

# Creating a multidimensional array using numpy
twodimlstnparrray = np.array(twodimlst)
print(type(twodimlstnparrray))
print(twodimlstnparrray)

# Converting a numpy array to a list
nparratolist = nparray.tolist()
print(type(nparratolist))
print(nparratolist)

# Creating a numpy array from a tuple
pytuple = (1,2,3,4,5)
print('pytuple type: ', type(pytuple))
print(pytuple)
nparrayfromtuple = np.array(pytuple)
print(type(nparrayfromtuple))
print(nparrayfromtuple)

# Shape of numpy array
print(nparray)
print(nparray.shape)
print(twodimlstnparrray.shape)

# Data type of numpy array
intlist = [-2, -1, 0 ,1 ,2]
intnparray = np.array(intlist)

floatnparray = np.array(intlist, dtype = float)
print(intnparray)
print(intnparray.dtype)
print(floatnparray)
print(floatnparray.dtype)

print('Size of nparray: ', nparray.size)
print('Size of two dimensional array: ', twodimlstnparrray.size)

# Mathematical operations using numpy

# Addition
nparrayplus10 = nparray + 10
print(nparrayplus10)

# Subtraction
nparrayorignal  = nparrayplus10 -10
print(nparrayorignal)

# Multiplication
nparraymul = nparray * 10
print(nparraymul)

# Division
nparraydiv = nparray / 10
print(nparraydiv)

# Modulus
nparraymod = nparray % 2
print(nparraymod)

# Floor division
nparrayfloor = nparray // 2
print(nparrayfloor)

# Exponential
nparrayexpo = nparray ** 2
print(nparrayexpo)

# Checking data types
print(intnparray.dtype)
print(floatnparray.dtype)
print(nparraybool.dtype)

# Getting items from numpy array
print(twodimlstnparrray[1])
print(twodimlstnparrray[:,0])
print(twodimlstnparrray[:,1])

# Slicing numpy array
firsttworowsandcolumns = twodimlstnparrray[0:2, 0:2]
print(firsttworowsandcolumns)

# Transpose a numpy array
nparraytranspose = twodimlstnparrray[::]
print(nparraytranspose)

# Reversing rown and columns
reversedrowsandcolumns = twodimlstnparrray[::-1, ::-1]
print(reversedrowsandcolumns)

# Printing a specific element in a 2d numpy array
print(twodimlstnparrray)
print(twodimlstnparrray[0,0]) # first element

# Numpy zeroes
npzeroes = np.zeros((3,3), dtype= int, order = 'C')
print(npzeroes)

npones = np.ones((3,3), dtype= int, order = 'C')
print(npones)

nptwos = npones * 2
print(nptwos)

# Reshape
# numpy.reshape(), numoy.flatten()
firstshape = np.array([(1,2,3), (4,5,6)])
print(firstshape)

reshaped = firstshape.reshape(3,2)
print(reshaped)

flattened = firstshape.flatten()
print(flattened)

# Horizontal stack
nplst1 = np.array([1,2,3])
nplst2 = np.array([4,5,6])

nplstsum = nplst1 + nplst2

print(nplstsum)

# hstack
print('Horizontal append: ', np.hstack((nplst1, nplst2)))

# vstack
print('Vertical append: ', np.vstack((nplst1, nplst2)))

# Generating random numbers

# Generate a random float number
randomfloat = np.random.random()
print(randomfloat)

# Generate a random 5 float numbers
randomfloat5 = np.random.random(5)
print(randomfloat5)

# Generate random integers in a specific range
randomint = np.random.randint(0,9)
print(randomint)

# Generate random number of integers in a specific range
randomint4 = np.random.randint(0,9, size = 4)
print(randomint4)

randintlst = randomint4.tolist()
print(randintlst)

# Numpy and statistics
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(nparray, color = "blue", bins = 40)
