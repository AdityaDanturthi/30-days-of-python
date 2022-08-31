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