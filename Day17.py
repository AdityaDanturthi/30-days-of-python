# Exception handling
from datetime import datetime

try:
    print(10 + '2')
except:
    print(' Something went wrong')

# Kind of error

try:
    name = input('Please input your name: ')
    birthyear = int(input('Please input your birth year: '))
    dateobj = datetime.now()
    thisyear = dateobj.year
    thisyear = int(thisyear)
    age = thisyear - birthyear
    print(f'Hi {name}! You are {age} years old.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')



