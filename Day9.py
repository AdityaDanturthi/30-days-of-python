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
