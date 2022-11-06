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

# Exercises: Level 1

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

# Sort the list using sort() method
ITCompanies.sort()
print(ITCompanies)

# Reverse the list in descending order using reverse() method
ITCompanies.sort(reverse= True)
print(ITCompanies)

# Slice out the first 3 companies from the list
firstthreeITcompanies = ITCompanies[:3]
print("First three IT companies:", firstthreeITcompanies)

# Slice out the last 3 companies from the list
lastthreeITcompanies = ITCompanies[-3:]
print("Last three IT companies:", lastthreeITcompanies)

# Slice out the middle IT company or companies from the list
middlecompany = int((len(ITCompanies)-1)/2)
print("Middle IT company:", ITCompanies[middlecompany])

# Remove the first IT company from the list
removedfirstcompany = ITCompanies.pop(0)
print("Removed first company:", removedfirstcompany)
print("New list:", ITCompanies)

# Remove the middle IT company or companies from the list
middlecompany = int((len(ITCompanies)-1)/2)
removedmiddlecompany = ITCompanies.pop(middlecompany)
print("Removed middle company:", removedmiddlecompany)
print("New list:", ITCompanies)

# Remove the last IT company from the list
removedlastcompany = ITCompanies.pop(-1)
print("Removed last company:", removedlastcompany)
print("New list:", ITCompanies)

# Remove all IT companies from the list
ITCompanies = []
print("IT companies list:", ITCompanies)

# Destroy the IT companies 
ITCompanies = ITCompanies.clear()
print(ITCompanies)

"""Join the following lists:

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']"""

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)

# After joining the lists in previous question. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
print(full_stack)

# Exercises: Level 2

#The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
agessorted = ages.copy()
print("Ages list sorted:", agessorted)
minage = min(ages)
print("Min age:", minage)
maxage = max(ages)
print("Max age:", maxage)

# Add the min age and the max age again to the list
ages.append(minage)
ages.append(maxage)
print("Added the min age and the max age again to the list", ages)

# Find the median age (one middle item or two middle items divided by two)
if (len(agessorted) % 2) == 0:
    middlenum1 = int((len(agessorted)-1)/2)
    middlenum2 = int(((len(agessorted)-1)/2)+1)
    print(f"Median ages: {agessorted[middlenum1]} and {agessorted[middlenum2]}")
else:
    median = int((len(agessorted)-1)/2)
    print("Median age:", agessorted[median])
    
# Find the average age (sum of all items divided by their number )
meanage = sum(agessorted)/len(agessorted)
print("Mean age:",meanage)

# Find the range of the ages (max minus min)
rangeofages = max(agessorted) - min(agessorted)
print("Range of age:", rangeofages)
# Compare the value of (min - average) and (max - average), use abs() method
mindiff = (min(agessorted) - meanage)
maxdiff = (max(agessorted) - meanage)
comparison = maxdiff > mindiff
print("Maxdiff > Mindiff:",comparison)

# Find the middle country(ies) in the countries list
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
]

middlecountry = int((len(countries)-1)/2)
print("Middle country:", countries[middlecountry])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
print("Length of countries list:", len(countries))
middlecountry = int((len(countries)-1)/2)
middlecountry += 1
firsthalf = countries[:middlecountry]
print(firsthalf)
secondhalf = countries[middlecountry:]
print(secondhalf)

"""['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries."""
randomcountries =['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
firstthreecountries = randomcountries[:3]
scandiccountries = randomcountries[3:]
print(firstthreecountries)
print(scandiccountries)
