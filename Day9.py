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
