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
print(fruits[1:3]) # excludes the first index

# Modifying a list
fruits[1] = 'pineapple'

# Checking if an item is in a list
doesitexist = 'pineapple' in fruits

# Adding items in a list
fruits.append('mango')

# Inserting items in a list
lst = ['item1','item2']
lst.insert(0,'item') # adds item in the beginning of the list

# Removing items from a list
lst.remove('item')

# removing items using index
lst.pop(0)

del lst[0] # same as .pop()

# Clearing a list
lst = ['item1','item2']
lst.clear() # removes all items

# Copying a list
fruits_copy = fruits.copy()



