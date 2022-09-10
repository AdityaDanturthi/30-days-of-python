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

# Creating a pandas series using linspace
s = pd.Series(np.linspace(5, 20, 10))
print(s)

# DataFrames 
# Creating a dataframe from a list of lists

data = [
    ['Aditya', 'Canada', 'NL'],
    ['Alex', 'Canada', 'QC']
]

listtodf = pd.DataFrame(data, columns = ['Name', 'Country', 'Province'])
print(listtodf)

# Creating a dataframe from a dictionary
dct  =  {
    'Name': ['Aditya', 'Alex'],
    'Country': ['Canada', 'Canada'],
    'Province': ['NL', 'QC']
}

dcttodf = pd.DataFrame(dct)
print(dcttodf)

# Creating dataframes from a list of dictionaries
lstofdcts =  [
    {'Name': 'Aditya', 'Country': 'Canada', 'Province': 'NL'},
    {'Name':'Alex', 'Country':'Canada','Province': 'QC'}
    ]
lstofdctstodf = pd.DataFrame(lstofdcts)
print(lstofdctstodf)