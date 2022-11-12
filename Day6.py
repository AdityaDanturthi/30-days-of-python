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

# Join fruits and vegetables tuples and assign it to fruitsandvegetables
fruitsandvegetables = fruits+vegetables
print("Fruits and vegetables:",fruitsandvegetables)

# How many fruits and vegetables do you have?
print(len(fruitsandvegetables))

# Exercises: Level 2

# Unpack fruits and vegetables from fruitsandvegetables
fruits1 = fruitsandvegetables[:2]
print("Fruits:",fruits1)
vegetables1 = fruitsandvegetables[2:]
print("Vegetables:",vegetables1)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
animalProducts = ('Milk', 'Cheese')
FoodsTuple = fruits1 + vegetables1 + animalProducts
print("Foods:",FoodsTuple)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
FoodsList = list(FoodsTuple)
print("Foods:",FoodsList)

# Slice out the middle item or items from the FoodsTuple tuple or FoodsList list
middleitem = int((len(FoodsList)-1)/2)
middleitem2 = middleitem + 1
print(f"Since the length of the list is {len(FoodsList)}, which is even. The two middle of the list are {FoodsList[middleitem]} and {FoodsList[middleitem2]}")

# Slice out the first three items and the last three items from FoodsList list
firstThreeinFoodsList = FoodsList[:3]
print(f"First three items in the list are {firstThreeinFoodsList}")

lastThreeinFoodsList = FoodsList[3:]
print(f"Last three items in the list are {lastThreeinFoodsList}")

# Delete the FoodsTuple tuple completely
del FoodsTuple

nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country
if 'Estonia' in nordicCountries:
    print("Estonia is in nordicCountries tuple")
else:
    print("Estonia is not in nordicCountries tuple")
    
# Check if 'Iceland' is a nordic country
if 'Iceland' in nordicCountries:
    print("Iceland is in nordicCountries tuple")
else:
    print("Iceland is not in nordicCountries tuple")
