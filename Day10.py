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
    print(key,value) # prints key and value

# for loop with set
ITcompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in ITcompanies:
    print(company)

# break and continue using for loop

for number in numbers:
    print(number)
    if number == 3:
        break

for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number is ', number + 1) if number != 5 else print('loop\'s end')
print('Outside loop')

# Range function
lst =list(range(11))
print(lst)

st = set(range(1,11))
print(st)

lst =list(range(0,11,2)) # step = 2
print(lst)

for number in range(11):
    print(number) # doesn't include 11

# Nested for loop

for key in dct:
    if key == 'skills':
        for skill in dct['skills']:
            print(skill)

# For else

for number in range(11):
    print(number)
else:
    print('Loop ends at:',number)

# Pass
for number in range(11):
    print(number)
    pass