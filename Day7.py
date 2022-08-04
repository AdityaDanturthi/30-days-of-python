# Sets: Collection of unordered and unindexed distinct elements

# Creating a set
from operator import le


st = {}
# or 
st = set()

# Example
fruits = {'banana','apple','orange', 'pineapple'}

# Length of a set
print(len(fruits))

# Accessing items in a set (Can only be accessed through loops)
for fruit in fruits:
    print('Fruits in the set: %s' %(fruit))

# Checking an item in a set
print('apple' in fruits) # True