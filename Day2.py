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
