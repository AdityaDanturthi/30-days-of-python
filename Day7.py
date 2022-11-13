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

# Exercises: Level 2

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Join A and B
C = A.union(B)
print(C)

# Find A intersection B
print(A.intersection(B))

# Is A subset of B
print(A.issubset(B))
print(B.issuperset(A))

# Are A and B disjoint sets
print(A.isdisjoint(B))

# What is the symmetric difference between A and B
print(B.symmetric_difference(A))

# Delete the sets completely
del A
del B

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ageSet = set(age)
print("Is the length of the list is greater than lenght of set:", len(age) > len(ageSet))

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence?"
sentenceSet = sentence.split()
print("Number of words in the sentence are:", len(sentenceSet))
