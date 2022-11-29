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

# Exercises: Day 11

# Exercises: Level 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
num1 = int(input("Please input the first number:"))
num2 = int(input("Please input the second number:"))

def addtwonumbers(a, b):
    return (a+b)

res = addtwonumbers(num1, num2)
print(f"{num1} + {num2} = {res}")

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
radius = float(input("Please input the radius of the circle:"))

def areaofcircle(r):
    area = 3.14 * r * r
    return area

area = areaofcircle(radius)

print(f"Area of circle with a radius of {radius} is {area}")

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def addition(*args):
    sum = 0
    for a in args:
        sum += a
    return sum
args = []
inputlen = int(input("How many number would you like to add? "))
for i in range(inputlen):
    args.append(int(input("Please input the number you would like to add: ")))

res = addition(*args)

print(f"The sum of {args} is {res}")
        
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def celciustofahrenheit(c):
    f = (c * (9/5)) + 32
    return f
c = float(input("Please input temperature in celsius to convert it into fahrenheit: "))
fahrenheit = celciustofahrenheit(c)

print(f"{c}°C -> {fahrenheit}°F")

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalized(lst):
    capitalizedlst = []
    for item in lst:
        temp = item.capitalize()
        capitalizedlst.append(temp)
    return capitalizedlst

lstlen = int(input("Please input the number of items you would like to input: "))
lst  = []
for i in range(lstlen):
    lst.append(input("Please input the element: ")) 

capitalizedlst = capitalized(lst)
print(capitalizedlst)

"""Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
food = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Pineapple'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      [2, 3, 7, 9, 5]"""

food = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2, 3, 7, 9];

def additem(lst, item):
    if lst == "food":
        item = item.capitalize()
        food.append(item)
        print(f"Added {item} to the {lst} list!")
        print("Updated list:",food)
    else:
        item = int(item)
        numbers.append(item)
        print(f"Added {item} to the {lst} list!")
        print("Updated list:",numbers)

lst = input("Please input the name of the list: ")
item = input("Please input the item: ")

additem(lst, item)

""" Declare a function named remove_item. It takes a list and an item as parameters. It returns a list with the item removed from it.
food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9];
print(remove_item(numbers, 3))  # [2, 7, 9]"""

food = ['Potato', 'Tomato', 'Mango', 'Milk'];
numbers = [2, 3, 7, 9];

def removeItem(lst, item):
    if lst == "food":
        item = item.capitalize()
        food.remove(item)
        print(f"Removed {item} from the {lst} list!")
        print("Updated list:",food)
    else:
        item = int(item)
        numbers.remove(item)
        print(f"Removed {item} from the {lst} list!")
        print("Updated list:",numbers)

lst = input("Please input the name of the list: ")
item = input("Please input the item to be removed: ")

removeItem(lst, item)

""" Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
print(sum_of_numbers(5))  # 15
print(sum_all_numbers(10)) # 55
print(sum_all_numbers(100)) # 5050"""

def addition(num):
    sum = 0
    for i in range(num+1):
        sum += i 
    return sum

num = int(input("Please input the upper limit of the range of number you want added:"))
res = addition(num)

print(f"The addition of all numbers upto {num} is {res}!")

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def additionOdd(num):
    sum = 0
    for i in range(num+1):
        temp = i
        if temp % 2 != 0:
            sum += temp 
    return sum

num = int(input("Please input the upper limit of the range of number you want added: "))
res = additionOdd(num)

print(f"The addition of all odd numbers upto {num} is {res}!")

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.

def additionEven(num):
    sum = 0
    for i in range(num+1):
        temp = i
        if temp % 2 == 0:
            sum += temp 
    return sum

num = int(input("Please input the upper limit of the range of number you want added: "))
res = additionEven(num)

print(f"The addition of all odd numbers upto {num} is {res}!")

# Exercises: Level 2

"""Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
    print(evens_and_odds(100))
    # The number of odds are 50.
    # The number of evens are 51."""
    
def numberOfEvenandOdd(num):
    counts = []
    countEven = 0
    countOdd = 0
    for i in range(num+1):
        if i % 2 == 0:
            countEven += 1
        else:
            countOdd += 1
    counts.append(countEven)
    counts.append(countOdd)
    return counts
num = int(input("Please input the upper limit of the range to find the number of even and odd numbers: "))

res = numberOfEvenandOdd(num)
print(res)
print(f"The number even numbers are {res[0]} and the number of odd numbers are {res[1]}")

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return fact

num = int(input("Please input a number to find it's factorial: "))
res = factorial(num)

print(f"The factorial of {num} is {res}")
