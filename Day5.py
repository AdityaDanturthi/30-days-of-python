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

# Joining lists
list1 = [1]
list2 = [2]
numbers = list1 + list2 # [1,2]

# Joining lists using extend()
list1.extend(list2) # [1,2]\

# Counting items in a list
list1.count(1) # 1

# Finding index of an item in a list
fruits.index('orange')

# Reversing a list
numbers.reverse() # [2,1]

# Sorting items in a list
numbers.sort() # ascending
numbers.sort(reverse=True) # descending

# sorted() returns the ordered list without modifying the original list
print(numbers.sorted())

# Exercises

# Declare an empty list
emptylist = []
print(emptylist)

# Declare a list with more than 5 items
fiveitemlist = [1,2,3,4,5]
print(fiveitemlist)

# Find the length of your list
print(len(fiveitemlist))

# Get the first item, the middle item and the last item of the list
print("First item:", fiveitemlist[0])
middleitem = int((len(fiveitemlist) -1)/2)
print("Middle item:", fiveitemlist[middleitem])
print("Last item:",fiveitemlist[-1])

# Declare a list called mixed_data_types, put your(name, age, height, marital status)
mixedlist = ["Aditya", 260, 6.0, "Single"]
print(mixedlist)

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
ITCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print("List of IT companies:",ITCompanies)

# Print the number of companies in the list
print("Number of IT companies int the list:",len(ITCompanies))

# Print the first, middle and last company
print("First company in the list is",ITCompanies[0])
middlecompany = int((len(ITCompanies) -1)/2)
print("Middle company in the list is",ITCompanies[middlecompany])
print("Last company in the list is",ITCompanies[-1])

# Print the list after modifying one of the companies
ITCompanies[5] = 'Netflix'
print("Update list of IT companies:", ITCompanies)

# Add an IT company to it_companies
ITCompanies.append('Oracle')
print(ITCompanies)

# Insert an IT company in the middle of the companies list
ITCompanies.insert(middlecompany, 'Alphabet')
print(ITCompanies)

# Change one of the it_companies names to uppercase (IBM excluded!)
ITCompanies[0] = ITCompanies[0].upper()
print(ITCompanies)

# Join the it_companies with a string '#;  '
ITCompaniescopy = ITCompanies.copy()
i = 0
while i < (len(ITCompanies)):
    ITCompaniescopy[i] = '#;  '+ITCompaniescopy[i]
    i = i + 1
print(ITCompaniescopy)

# Check if a certain company exists in the it_companies list.
if 'Google' in ITCompanies:
    print('Google is in ITCompanies')
