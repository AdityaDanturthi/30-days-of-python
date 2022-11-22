# Conditional statements

# if condition

# syntax
# if condition:
#     statement to execute if true

# if example
a = 3
if a > 2:
    print('a is greater than 2')

# if-else
if a > 3:
    print('a is greater than 3')
elif a ==3:
    print('a is equal to 3')
elif a < 3:
    print('a is less than 3')

# Short hand
# code if condition else
a = 3
print('a is greater than 2') if a > 2 else print('a is less than 2')

# Nested if
b = 0
if b > 0:
    if b%2 == 0:
        print('b is a positive and even number')
    else:
        print('b is a positive number')
elif b == 0:
    print('b is 0')
else:
    print('b is a negative number')

# if conditon in combination with logical operators
if b > 0 and b%2 == 0:
    print('b is a positive and even number')
elif b > 0 and b%2 != 0:
    print('b is a positive and odd number')
elif b == 0:
    print('b is zero')
else:
    print('b is a negative number')

# if and or logical operator
user = 'admin'
accesslevel = 3
if user == 'admin' or accesslevel == 3:
    print('Access granted!')
else:
    print('Access denied!')

# Exercises: Day 9

# Exercises: Level 1

# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
"""Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive."""

age = int(input("Please enter your age:"))
if age >= 18:
    print("You are old enough to drive!")
else:
    temp = age
    diff = 18 - temp
    print(f"You can drive in {diff} year(s)!")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
"""Enter your age: 30
You are 5 years older than me."""

age = 26
userage = int(input("Please enter your age:"))

temp = userage
diff = age - temp
diff = abs(diff)

if userage < age:
    print(f"You are {diff} year(s) younger than me!")
elif userage == age:
    print("We are the same age!")
elif userage > age:
    print(f"You are {diff} year(s) older than me!")

# Exercises: Level 2

"""Write a code which gives grade to students according to theirs scores:

80-100, A
70-89, B
60-69, C"""

score = int(input("Please input your score:"))
if score in range(80,101):
    print("Grade: A")
elif score in range(70,90):
    print("Grade B")
elif score in range(60,70):
    print("Grade C")

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

autumn =['september', 'october', 'november']
winter = ['december', 'january', 'february']
spring = ['march', 'april', 'may']
summer = ['june', 'july', 'august']

month = input("Please input a month to know the season:")

if month in autumn:
    print("Autumn!")
elif month in winter:
    print("Winter!")
elif month in spring:
    print("Spring!")
elif month in summer:
    print("Summer!")
