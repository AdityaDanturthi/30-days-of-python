# Loops

# While loop
count= 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

# break and continue
count = 0
while count < 5:
    print(count) # print 0, 1, 2
    count += 1
    if count == 3:
        break

count = 0
while count < 5:
    print(count) # print 0, 1, 2, 4 (skips 3)
    count += 1
    if count == 3:
        continue
    print(count)
    count += 1

# For loop
numbers = [0,1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    print(number)

# for loop with string

language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])

# for loop with tuple
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)

# for loop with dictionary looping through a dictionary gives you the key from the dictionary

dct = {
    'name':'Aditya',
    'age':260,
    'skills':['JavaScript', 'Python', 'Power BI', 'SQL', 'Tableau'],
    'address':{
        'street':'this street',
        'zipcode':'A1B C2D'
    }
}

for key in dct:
    print(key) # prints keys in the dictionary

for key,value in dct.items():
    print(key,value)