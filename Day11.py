# Functions

# Declaring a function without parameters or return
from email import message


def fullname():
    firstname = 'Aditya'
    lastname = 'Danturthi'
    name = firstname+' '+lastname
    print(name)
fullname()

# Declaring a function with return but without parameters 

def fullnamereturn():
    firstname = 'Aditya'
    lastname = 'Danturthi'
    return firstname+' '+lastname
print(fullnamereturn())

def addtwonumbers():
    num1 = 1
    num2 = 2
    return num1 + num2
print(addtwonumbers())


# Declaring a function with return and parameters 
def greeting(name1):
    greetingmessage = name1+', How are you?'
    return greetingmessage
name1 = input('Please input your name: ')
print(greeting(name1))