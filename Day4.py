# Strings
letter ='p' # string variable
print(letter) # p
print(len(letter)) # 1
greeting = 'Hello, World!'
print(greeting) # Hello, World!
print(len(greeting)) # 13
sentence = 'I am enjoying 30 days of python'
print(sentence)
print(len(sentence)) # 31

# Declaring multiline strings
multiline_string = '''I am a programmer and enjoy programming.
It is rewarding to do what you are passionate about.
That is why I am doing 30 days of python'''
print(multiline_string)

# Multiline string using double quotes
multiline_string = """I am a programmer and enjoy programming.
It is rewarding to do what you are passionate about.
That is why I am doing 30 days of python"""
print(multiline_string)

# String concatenation
firstname = 'Aditya'
lastname = 'Danturthi'
space = ' '
fullname = firstname+space+lastname
print(fullname) # Aditya Danturthi
print(len(firstname)) # 6
print(len(lastname)) # 9
print(len(firstname) > len(lastname)) # True
print(len(fullname)) # 16

# Escape sequences in strings

# \n: New line
# \t: Tab (8 spaces)
# \\: Back slash
# \': Single quote (')
# \": Double quote (")

print(" I am enjoying \t\n The \'python challenge\'")

# String formatting

firstname = 'Aditya'
lastname = 'Danturthi'

formattedstring ='I am %s %s !' %(firstname,lastname)
print(formattedstring)

# New formatting 
a = 1
b = 2
print("{} + {} = {} ".format(a,b,a+b))

print("I am {} {} !".format(firstname,lastname))

# String interpolation or F-strings
print(f'{a} + {b} = {a+b}')

# Python strings as a sequence of characters

language ='Python'
a,b,c,d,e,f = language
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n


# Accessing characters in strings by index

firstletter =language[0]
print(firstletter) # P
lastletter = language[-1]
print(lastletter)

# Slicing strings in python

firstThreeLetters = language[0:3]
print(firstThreeLetters)
lastThreeLetters = language[-3:]
print(lastThreeLetters)
lastThreeLetters = language[3:]
print(lastThreeLetters)
lastThreeLetters = language[3:6]
print(lastThreeLetters)

# Reversing a string

print(greeting[::-1]) # !dlroW, olleH

# SKipping characters while slicing
print(language[0:6:2])

# String methods:

#capitalize
challenge = "thirty days of python"
print(challenge.capitalize())

#count
print(challenge.count('y')) # 3
print(challenge.count('y',7,14)) # 1
print(challenge.count('th')) # 2

#endswith()
print(challenge.endswith('on')) # True
print(challenge.endswith('tion')) # False

# expandtabs(): replaces spaces with tabs
print(challenge.expandtabs()) # replace space with 8 spaces by default
print(challenge.expandtabs(10)) # replace space with 10 spaces4

# find() returns first occurrence of a substring or else it will return -1
print(challenge.find('y')) # 5
print(challenge.find('th')) # 0

# rfind() returns last occurrence of a substring or else it will return -1
print(challenge.rfind('y')) # 16
print(challenge.rfind('th')) # 17

country ='Canada'
age = 250
# format(): formatting the output string
sentence = 'I am {} {}. I live in {}. I am {} old.'.format(firstname,lastname,country,age)

radius = 10
pi = 3.14 
area = pi*radius**2
result = 'The radius of the circle is {} and the area is {}'.format(str(radius),str(area))

# index(): returns the lowest index of a substring
substring = 'da'
print(challenge.index(substring))

# rindex(): returns the highest index of a substring
substring = 'da'
print(challenge.rindex(substring))

# isalnum(): checks if there's a alphanumeric character
challenge = "30DaysofPython"
print(challenge.isalnum()) # True

challenge = "30 Days of Python"
print(challenge.isalnum()) # False

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
concatstr = str1 +" "+str2+" "+str3+" "+str4
print(concatstr)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
strr1 = 'Coding'
strr2 = 'For'
strr3 = 'All'
concstr = strr1+" "+strr2+" "+strr3
print(concstr)

# Declare a variable named company and assign it to an initial value "Coding For All".
company  = "Coding For All"
# Print the variable company using print().
print(company)
