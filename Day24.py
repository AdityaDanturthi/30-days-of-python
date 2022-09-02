# Statistical Analysis

# Numpy
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