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