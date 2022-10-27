# Boolean
print(True)
print(False)

# Types of operators

# Assignment operators
x = 5
x +=3
x -= 3
x *= 3
x /= 3
x %= 3


# Arithmetic operators
print('Addition: ', 1+2)                     # 3
print('Subtraction: ', 2-1)                  # 1
print('Multiplication: ', 2*3)               # 6
print('Division: ', 4/2)                     # 2.0 python gives floating by default
print('Division without remainder: ', 7//2)  # 3
print('Modulus: ', 3%2)                      # 1 gives the remainder
print('Exponentiation: ', 3**2)              # 9 (3*3)



# Exercises
age = 260
height = 6.0
complex = 1+3j
base = input('Please input base of the triangle: ')
heightoftriangle = input('Please input height of the triangle: ')
print('Area of triangle: ', 0.5* float(base)*float(heightoftriangle))

a,b,c = input('Please input 3 sides of the triangle to calculate it\'s perimeter: ')
print('Perimeter: ',a+b+c)

print(len('python') > len('dragon'))
print('on' in 'python' and 'dragon')
print('10' is 10)

hours = input('Hours: ')
rate = input('Rate: ')
print('Weekly earnings: ', hours*rate)

# Rectangle: Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenofrectangle, widthofrectangle = input("Please input length and widht of the rectangle: ")
areaofrectangle = lenofrectangle * widthofrectangle
print("Area of rectagle: ", areaofrectangle)
perimeterofrectangle = 2 * (lenofrectangle + widthofrectangle)
print("Perimeter of rectagle: ", areaofrectangle)

# Circle: Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
radius = input("Please input radius of the circle: ")
area = pi*radius^2
print("Area of circle: ",area)
circumference = 2*pi*radius
print("Circumference of the circle: ", circumference)

# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
for x in range(-1,-100,-1):
    y = x*x + 6*x + 9
    if y == 0:
        print(f"y = 0 at x = {x}")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if (len('python') == len('dragon')):
    print('python and dragon are of the same length')
else: 
    print('python and dragon are not of the same length')
    
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if ('on' in 'python' and 'dragon'):
    print('yes')
else: 
    print('no')
    
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon."
if ('jargon' in sentence):
    print('Yes!')
else:
    print("No!")
    
# Find the length of the text python and convert the value to float and convert it to string.
lenvar = len('python')
print('Lenght of python in int = ', lenvar)
lenfloat = float(lenvar)
print('Lenght of python in float = ', lenfloat)
string = str(lenfloat)
print(f"{lenfloat} is of type:", type(string))
