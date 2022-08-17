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

#  Using date from datetime
d = date(2022,1,1)
print(d)

print('Current date:', d.today())

# Date object of today's date
today = date.today()
print('Current year: ', today.year)
print('Current month: ', today.month)
print('Current day: ', today.day)

# Time objects to represent time
from datetime import time

a = time()
print('Time:',a)

b = time(10,30,50) # time(hours, minutes, seconds)
print(b)

c = time(hour = 10, minute = 50, second = 5)
print(c)

d = time(10,50,5, 100000) # last parameter is microseconds
print(d)

# Difference between two points in time
today = date(year = 2022, month = 8, day= 17)
newyear = date(year = 2023, month = 1, day= 1)

daystonewyear =  newyear-today

tt = datetime(year = 2022, month = 8, day =17, hour = 0, minute = 0, second = 59)
tt1 = datetime(year = 2022, month = 10, day =18, hour = 0, minute = 0, second = 59)

ttdiff = tt1-tt
print(ttdiff)

print('Days to new year: ',daystonewyear)

# Difference between two points in time using timedata
from datetime import timedelta
td = timedelta(weeks = 12, days = 10, hours= 4, seconds= 20)
td1 = timedelta(days = 7, hours = 5, minutes= 3, seconds= 30)
tddiff = td - td1
print(tddiff)