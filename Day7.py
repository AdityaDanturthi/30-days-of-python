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

# Sets
ITCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1

# Find the length of the set ITCompanies
print("Length of ITCompanies set:",len(ITCompanies))

# Add 'Twitter' to ITCompanies
ITCompanies.add('Twitter')
print(ITCompanies)

# Insert multiple IT companies at once to the set ITCompanies
ITCompanies.update(['Salesforce', 'Atlassian'])
print(ITCompanies)

# Remove one of the companies from the set ITCompanies
ITCompanies.remove('Facebook')
print(ITCompanies)

# What is the difference between remove and discard
# Remove throws an error if the item being removed is not present in the set. Discard in the other hand doesn't throw an error even if the item being removed is not present in the set.
