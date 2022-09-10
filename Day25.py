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

hwdf = pd.read_csv('weight-height.csv')

# Data exploration
print(hwdf.head())
print(hwdf.tail())

print(hwdf.shape)

print(hwdf.columns)

heights = hwdf['Height']
print(heights)

weights = hwdf['Weight']
print(weights)

print(len(heights) == len(weights))

print(heights.describe())
print(weights.describe())

print(hwdf.describe())

# Modifying a dataframe

# Adding a new column
df = dcttodf.iloc[:,1:3]
df['Name'] = ['A', 'B']
heightdata =  [170,171]
weightdata = [70,71]
df['Weight'] = weightdata
df['Height'] = heightdata
print(df)

df['Height'] = df['Height'] * 0.01
print(df)

def bmicalc():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi

bmi = bmicalc()

df['BMI'] = bmi
print(df)

# Formatting a column
df['BMI'] = round(df['BMI'], 2)
print(df)

df['birthyear'] = [1990, 1991]
df['currentyear'] = 2022
namecol = df.pop('Name')
df.insert(0,namecol.name, namecol)
print(df)

# Checking data types of columns
print(df.Weight.dtype)
print(df.Height.dtype)

df['birthyear'] = df['birthyear'].astype('int')
print(df['birthyear'].dtype)

df['currentyear'] = df['currentyear'].astype('int')
print(df['currentyear'].dtype)

df['Age'] = df['currentyear'] - df['birthyear']
print(df)