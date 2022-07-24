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