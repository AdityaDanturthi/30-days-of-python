# Tuples
# Tuples are written with round brackets (). 

# Creating a tuple
empty_tuple = tuple()


fruits = ('apple','banana', 'orange', 'mango')
print(len(fruits)) # lenght of tuple

# Accessing items in a tuple

firstfruit = fruits[0]
lastfruit = fruits[-1]

# Converting tuple into a list
fruits = list(fruits)

# Converting list to a tuple
fruits = tuple(fruits)

# Checking if an item is in a tuple
'apple' in fruits # Returns true

# Joining multiple tuples
morefruits = ('pineapple', 'watermelon')

fruits = fruits + morefruits

# Deleting items in a tuple (Note:It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.)
del fruits

# Exercises: Level 1

# Create an empty tuple
emptyTuple =()
# Create a tuple containing fruits and vegetables
fruits = ('Apple', 'Pineapple')
vegetables = ('Cauliflower', 'Broccoli')

# Join fruits and vegetables tuples and assign it to fruitsandvegetables
fruitsandvegetables = fruits+vegetables
print(fruitsandvegetables)

# How many fruits and vegetables do you have?
print(len(fruitsandvegetables))
