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

# Adding itmes in a set
fruits.add('mango')

# Adding multiple fruits to a set
morefruits = ('watermelon', 'avocado')
fruits.update(morefruits)

# Removing items from a set
fruits.remove('mango')

fruits.add('mango')

# Removing an item from a set using pop(). pop() removes a random item in the list
removeditem = fruits.pop()