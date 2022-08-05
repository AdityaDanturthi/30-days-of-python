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

# Clearing items in a set
fruits.clear()

fruits = {'banana','apple','orange', 'pineapple'}

# Deleting a set
del fruits

fruits = {'banana','apple','orange', 'pineapple'}

# Converting a list into a set
vegetables = ['tomato', 'potato', 'cabbage','onion', 'carrot']
vegetables = set(vegetables)

# Joining sets
fruitsandvegetables = fruits.union(vegetables)

# Finding intersection of items in a set
fruits = fruits.intersection(fruitsandvegetables)

# Checking superset and subset
print(fruits.issubset(fruitsandvegetables)) # True
print(fruitsandvegetables.issuperset(fruits)) # True

# Checking differences between two sets
print(fruits.difference(fruitsandvegetables))

# Finding symmetric differences bewteen sets
print(fruitsandvegetables.symmetric_difference(fruits))

# Disjoint sets: If two sets don't have anythong in common they are called disjoint sets
fruits.isdisjoint(vegetables) # True