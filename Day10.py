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

# Exercises: Level 1

#Iterate 0 to 10 using for loop, do the same using while loop.
print("For Loop\n")
for i in range(0,11):
    print(f"{i}\n")

print("While Loop\n")
i = 0
while i <11:
    print(f"{i}\n")
    i += 1
    
#Iterate 10 to 0 using for loop, do the same using while loop.
print("Reverse For Loop\n")
for i in range(10,-1,-1):
    print(f"{i}\n")
    
print("Reverse While Loop\n")
i =10
while i >= 0:
    print(f"{i}\n")
    i -= 1

    # Write a loop that makes seven calls to print(), so we get on the output the following triangle:

  #
  ##
  ###
  ####
  #####
  ######
  #######

print("First Pattern:")
for i in range(8):
    for j in range(i):
        print("#", end = '')
    print(" ")

# Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

print("Second Pattern:\n")
for i in range(8):
    for j in range(8):
        print("#", end = ' ')
    print(" ")

"""Print the following pattern:

0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""

for i in range(11):
        temp = i*i
        print(f"{i} x {i} = {temp}")
print()

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.

langlist = ['Python', 'Numpy','Pandas','Django', 'Flask']
for l in langlist:
    print(l)

# Use for loop to iterate from 0 to 100 and print only even numbers
print("Even numbers between 0 and 100:")
for i in range(0,100,2):
    print(i)

# Use for loop to iterate from 0 to 100 and print only odd numbers
print("Odd numbers between 0 and 100:")
for i in range(1,101,2):
    print(i)
    
# Exercises: Level 2

# Use for loop to iterate from 0 to 100 and print the sum of all numbers. The sum of all numbers is 5050.
sum = 0
for i in range(0,101):
    sum += i
print("Sum of all numbers from 0 to 100 is:", sum)


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds. The sum of all evens is 2550. And the sum of all odds is 2500.
evensum = 0
for i in range(0,101, 2):
    evensum += i
print("Sum of all even numbers from 0 to 100 is:", evensum)

oddsum = 0
for i in range(1,101, 2):
    oddsum += i
print("Sum of all odd numbers from 0 to 100 is:", oddsum)

# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

names = []
for i in countries:
    if "land" in i:
        names.append(i)
print(f"The countries with \"land\" in their name are {names}")

# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']

lenFruits = len(fruits)-1
reverseFruits = []
for i in range(lenFruits, -1, -1):
    reverseFruits.append(fruits[i])
print(reverseFruits)

