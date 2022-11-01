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

# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
firstletter = company[0]
print(firstletter)
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
if 'Coding' in company:
    print('True')
else:
    print('False')
# Replace the word coding in the string 'Coding For All' to Python.
newstr = company.replace('Coding','Coding is')
print(newstr)
# Change Python for Everyone to Python for All using the replace method or other methods.
orgstr = 'Python for Everyone'
newstrr = orgstr.replace('Python for Everyone','Python for All')
print(newstrr)
# Split the string 'Coding For All' using space as the separator (split()) .
w = company.split()
print(w)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
topcompanies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
separate = topcompanies.split(sep = ',')
print(separate)

# What is the character at index 0 in the string Coding For All.
firstchar = company[0]
print("The charater at index 0 in Coding For All is", firstchar)

# What is the last index of the string Coding For All.
lastchar = company[-1]
print("The last charater in Coding For All is", lastchar)

# What character is at index 10 in "Coding For All" string.
charatindex10 = company[10]
print("The charater at index 10 in Coding For All is", charatindex10)

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = 'Python For Everyone'
abbr = pfe[0]+pfe[7]+pfe[11]
print("Abbreviation for Python For Everyone is: ", abbr)

# Create an acronym or an abbreviation for the name 'Coding For All'.
abb = company[0]+company[7]+company[11]
print("Abbreviation for Coding For All is: ", abb)

# Use index to determine the position of the first occurrence of C in Coding For All.
positionofc = company.find('C')
print("C is at index:", positionofc)

# Use index to determine the position of the first occurrence of F in Coding For All.
positionoff = company.find('F')
print("F is at index:", positionoff)

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
positionoflastl = company.rfind('l')
print("Last of l is at index:", positionoflastl)

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
firstbecause = sentence.find('because')
print('First occurence of because is at:', firstbecause)

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
import re
cleansentence = sentence.replace("because",'').replace("is", '')
cleansentence = re.sub("\s\s+" , " ", cleansentence)
print(cleansentence)

# Does 'Coding For All' start with a substring Coding?
print("Coding For All starts with Coding is:", company.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print("Coding For All ends with Coding is:", company.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
stringwithspaces = '   Coding For All      ' 
print(stringwithspaces.strip())

""" Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python """
str1 = "30DaysOfPython"
str2 = "thirty_days_of_python"

checkstr1 = str1.isidentifier()
checkstr2 = str2.isidentifier()

print("Is 30DaysOfPython an identifier? :", checkstr1)
