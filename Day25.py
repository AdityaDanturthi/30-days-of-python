# Pandas

import pandas as pd
import numpy as np

# Creating a pandas series with default index
nums = [1,2,3,4,5]
pandaseries = pd.Series(nums)
print('Type: ', type(pandaseries))
print(pandaseries)

# Creating a pandas series with custom index
serieswithcustomindex = pd.Series(nums, index = [1,2,3,4,5])
print(serieswithcustomindex)

fruits = ['apple', 'pineapple', 'orange']
fruitsseries = pd.Series(fruits, index= [1,2,3])
print(fruitsseries)

# Creating a pandas series from a dictionary
dct = {'name': 'Aditya', 'country': 'Canada', 'age': 260}
dcttoseries = pd.Series(dct)
print(dcttoseries)

# Creating a constant pandas series
constantseries = pd.Series(2, index= [1,2,3,4,5])
print(constantseries)