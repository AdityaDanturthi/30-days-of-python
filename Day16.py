# Datetime module

import datetime
from sqlite3 import Timestamp
from time import time
print(dir(datetime))

# Getting date time information
from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

print(day, month, year, hour, minute, second)
print('Timestamp: ', timestamp)
