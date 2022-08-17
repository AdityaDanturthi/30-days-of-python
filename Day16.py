# Datetime module

import datetime
from sqlite3 import Timestamp
from time import strftime, time
print(dir(datetime))

# Getting date time information
from datetime import datetime
now1 = datetime.now()
day = now1.day
month = now1.month
year = now1.year
hour = now1.hour
minute = now1.minute
second = now1.second
timestamp = now1.timestamp()

print(day, month, year, hour, minute, second)
print('Timestamp: ', timestamp)

print(f'{day}/{month}/{year}, {hour}:{minute}')

# New Year

from datetime import datetime
newyear = datetime(2022,1,1)
print(newyear)
day = newyear.day
month = newyear.month
year = newyear.year
hour = newyear.hour
minute = newyear.minute
second = newyear.second

print(day, month, year, hour, minute, second)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formatting date output using strftime

from datetime import *
now2 = datetime.now()
t = now2.strftime('%H:%M:%S')
print('Time: ',t)

t1 = now2.strftime("%m-%d-%Y, %H:%M %p")
print(t1)

t2 = now2.strftime("%d-%m-%Y, %H:%M %p")
print(t2)

# String to time using strptime
datestr = '1 January, 2022'
print('Date string: ',datestr)

dateobj = datetime.strptime(datestr, '%d %B, %Y')

print('Date object: ',dateobj)