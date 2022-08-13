# List comprehension
# syntax: [i for i in iterable if expression]

# Ways to convert a string to a list of characters
language = 'Python'
lst = list(language)
print(type(lst))
print(lst)

lst1 = [i for i in language]
print(type(lst1))
print(lst1)

# Generating a list of numbers
numlst = [i for i in range(11)]
print(type(numlst))
print(numlst)

# Perofrming mathematical operations while creating a list using list comprehension
squarslst = [i*i for i in range(11)]
print(type(squarslst))
print(squarslst)