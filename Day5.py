# Lists

"""
There are four collection data types in Python :

List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
 """
# Creating a list
lst = list() # This is an empty list

# Using square brackets
lst = [] # This is an empty list

fruits = ['apple','mango','banana','orange']
print('Fruits: ', fruits)

print('Number of fruits: ',len(fruits))
 
 # list can have different types of data
listprop = ['Aditya',260,True,{'Hi': 'How are you?'}]

# Accessing lists using indexing
print(fruits[0])

# Unpacking list items
item1, item2, itmem3, item4 = fruits

# Slicing items in a list
print(fruits[0:4]) # returns all fruits
print(fruits[0:]) # returns all fruits