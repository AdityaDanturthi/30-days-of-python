from random import *
from string import *
import string

def userid(numberofstringsreq, numberofchars):
    useridstringlist = []
    i = 0
    while i < numberofstringsreq:
        useridstring = ''
        while len(useridstring) < numberofchars:
            randomnumber = randint(0,9)
            randomletter = choice(string.ascii_letters)
            randomnumber = str(randomnumber)
            randomstring = choice(randomnumber+randomletter)
            useridstring += randomstring 
        useridstringlist.append(useridstring)
        i += 1 
    return useridstringlist

numberofchars = int(input('Number of characters required:'))
numberofstringsreq = int(input('Number of strings required:'))
print(userid(numberofstringsreq, numberofchars))














