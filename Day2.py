# Built-in functions and variables

print("Hello, world!") # prints the string between the quotes
len('Hello, world!') # prints the length of the string
type('Hello, world!') # prints the datatype
str(10) # converts the number into a string
int('10') # converts the string into int
float(10) # converts int into float
input('Enter your name') #accepts input

min(10,20,30,40,50) # returns the minimum value
max(10,20,30,40,50) # returns the maximum value
min([10,20,30,40,50]) # takes list as an argument and returns the minimum value
max([10,20,30,40,50]) # takes list as an argument and returns the maximum value
sum([10,20,30,40,50]) # takes list as an argument and returns the sum


# Variables

first_name = 'Aditya'
last_name = 'Danturthi'
country = 'Canada'
age = 260
is_married = False
skills = ['HTML', 'CSS', 'JS', 'SQL', 'Python']
person_info = {
   'firstname':'Aditya',
   'lastname':'Danturthi',
   'country':'Canada',
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables on a single line
first_name, last_name, country, age, is_married = 'Aditya', 'Danturthi', 'Canada', 260, False


# User input
first_name = input('What is your name: ')
age = input('How old are you? ')

print(first_name)
print(age)

# Checking data types and Casting

first_name = 'Aditya'     # str
last_name = 'Danturthi'   # str
country = 'Canada'         # str
age = 260                  # int

# Printing out types
print(type('Aditya'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Aditya','age':260, 'is_married':False}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

# Type casting

# int to float
num_int = 10
print('num_int',num_int)         # 10
num_float = float(num_int)
print('num_float:', num_float)   # 10.0

# float to int
gravity = 9.81
print(int(gravity))             # 9

# int to str
num_int = 10
print(num_int)                  # 10
num_str = str(num_int)
print(num_str)                  # '10'

# str to int or float
num_str = '10.6'
print('num_int', int(num_str))      # 10
print('num_float', float(num_str))  # 10.6

# str to list
first_name = 'Aditya'
print(first_name)               # Aditya
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 'd', 'i', 't', 'y', 'a']