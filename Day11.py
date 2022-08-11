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
    greetingmessage = 'Hi '+name1+'! How are you?'
    return greetingmessage
name1 = input('Please input your name: ')
print(greeting(name1))

def addten(num2):
    return num2+10
print(addten(90))

def squareanumber(num3):
    return num3 ** 2
print(squareanumber(2))

def areaofcircle(r):
    area = 3 * 3.14 * r ** 2
    return area
print(areaofcircle(10))

def sumofnumbers(n):
    total = 0
    for i in range(n+1):
        total += i
    print(total)
sumofnumbers(10)

# Multiple parameters in a function
def printfullname(firstname1,lastname1):
    fullname1 = firstname1+' '+lastname1
    return fullname1
print(printfullname('Aditya','Danturthi'))

def agecalculator(currentyear,birthyear):
    age = abs(currentyear-birthyear)
    return age
print('Age: ',agecalculator(1996,2022))

def weightinnewtons(mass, gravity):
    weight = mass*gravity
    weight = round(weight,2)
    weight = str(weight)+'N'
    return weight
print('Weight in Newtons: ',weightinnewtons(80,9.81))

# Passing arguments with key and value
def printfullname2(firstname2,lastname2):
    fullname2 = firstname2+' '+lastname2
    return fullname2
print(printfullname2(firstname2='Aditya',lastname2='Danturthi'))

# Functions with default parameters
def greetings(name2 = 'Aditya'): # Default value of the parameter
    message2 = name2 + ', How\'s it going?'
    return message2
print(greetings('Adi')) # Parameter passed with fuction call overrides default paramenter

# Arbitrary number of arguments: If we do not know the number of arguments we pass to our function, we can create a function which can take arbitrary number of arguments by adding * before the parameter name.
def sumofmultiplenumbers(*nums):
    total1 = 0
    for num2 in nums:
        total1 += num2
    return total1
print(sumofmultiplenumbers(1,2,3,4,5,6,7,8,9,10))

# Default and arbitrary number of arguments in functions
def numbergenerator(team, *args):
    print(team)
    for i in args:
        print(i)
numbergenerator('Team 1', 'Aditya', 'Alex')