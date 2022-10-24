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



#Exercises
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

# Rectangle
lenofrectangle, widthofrectangle = input("Please input length and widht of the rectangle: ")
areaofrectangle = lenofrectangle * widthofrectangle
print("Area of rectagle: ", areaofrectangle)
perimeterofrectangle = 2 * (lenofrectangle + widthofrectangle)
print("Perimeter of rectagle: ", areaofrectangle)

# Circle
pi = 3.14
radius = input("Please input radius of the circle: ")
area = pi*radius^2
print("Area of circle: ",area)
circumference = 2*pi*radius
print("Circumference of the circle: ", circumference)
