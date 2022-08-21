# Regular Expressions: It is a special text string that helps find patterns in data
import email
from gettext import find
import re

# re.match() : searches only the beginning of the first line of the string and returns the matched object or returns none 
txt = 'I love python'
match = re.match('I love python', txt, re.I) # re.I ignores case
print(match) # returns only if the text starts with the pattern

span = match.span() # index starting ending characters of the matched string
print(span)
startmatchchar, endmatchchar = span
print(startmatchchar, endmatchchar)
substr = txt[startmatchchar:endmatchchar]
print(substr)

# re.search(): returns matched object from anywhere in the string including multiline strings 
txtsearch = '''Python is the most beautiful language that a human being has ever created.
I recommend python.'''

search = re.search('recommend', txtsearch, re.I)
print(search)
spansearch = search.span()
print(spansearch)
startsearchchar, endsearchchar = spansearch
print(startsearchchar,endsearchchar)
searchsubstr = txtsearch[startsearchchar:endsearchchar]
print(searchsubstr)

# re.findall(): returns a list containing all matches
findalltxt = '''Python is the most beautiful language that a human being has ever created.
I recommend python.'''

findall = re.findall('python',findalltxt, re.I)
print(findall)

# Including all cases without re.I
findall1 = re.findall('[Pp]ython',findalltxt)
print(findall)

# re.sub(): replaces one or many matches with a string
txt1 = '''Python is the most beautiful language that a human being has ever created.
I recommend python.'''

strreplace = re.sub('Python|python','Javascript',txt1, re.I)
print(strreplace)

# or

strreplace1 = re.sub('[Pp]ython','Javascript',txt1)
print(strreplace1)

txt2 = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

easystr = re.sub('%', '', txt2)
print(easystr)

# re.split(): takes a string, splits it at the match points, returns a list
print(re.split('\n',easystr)) # returns a list with split strings

# Writing RegEx patterns: for declaring a str variable we use single or double quotes, However, to declare a regex variable we use r''.

regexapple = r'apple'
txtfruits = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regexapple, txtfruits)
print(matches)

# To ignore the case and include all matches
matchescaseinsensitive = re.findall(regexapple, txtfruits,re.I)
print(matchescaseinsensitive)

regexapplebothcases = r'[Aa]pple'
matchescaseinsensitive1 = re.findall(regexapplebothcases, txtfruits)
print(matchescaseinsensitive1)

# Square bracket
fruitsstr = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
applematches = re.findall(regexapplebothcases, fruitsstr)
print(applematches)

regexappleandbanana = r'[Aa]pple | [Bb]anana'
appleandbananamatches = re.findall(regexappleandbanana, fruitsstr)
print(appleandbananamatches)

# Escape characters(\) in regex
regexescape = r'\d' # d is a special character and stands for digits
strwithnums = 'This regular expression example was made on August 20,  2022 and revised on August 20, 2022'
nummatches = re.findall(regexescape, strwithnums)
print(nummatches)

# Find and searatre numbers by number of digits
regexescape = r'\d+' # d is a special character and stands for digits
strwithnums1 = 'This regular expression example was made on August 20,  2022 and revised on August 20, 2022'
nummatches1 = re.findall(regexescape, strwithnums1)
print(nummatches1)

# Period(.)
regexpatper = r'[a].' # a in square brackets followed by a . means any character except new line character
matchesper = re.findall(regexpatper, fruitsstr)
print(matchesper)

# Zero or more times(*)
fruitsstr1 = '''Apple and banana are fuits''' # . any character, + any character one or more times 
regexreppatper = r'[a].*'
mulmatches = re.findall(regexreppatper, fruitsstr1)
print(mulmatches)

# Zero or one time(?)
emailtxt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regexem = r'[Ee]-?mail' # ? means that - is optional
matchesem = re.findall(regexem, emailtxt)
print(matchesem)

# Quantifier in regex: specify the length of substring we are looking for in a textquanttxt = 
strwithnums = 'This regular expression example was made on August 20,  2022 and revised on August 20, 2022'
regexquant = r'\d{4}'
yearsinthestr = re.findall(regexquant, strwithnums)
print(yearsinthestr)

regexyearanddays = r'\d{1,4}'
dayandyearsinstr = re.findall(regexyearanddays, strwithnums)
print(dayandyearsinstr)

# Cart ^: starts with
regexstartswith = r'^This'
startswithmatch = re.findall(regexstartswith, strwithnums)
print(startswithmatch)

# Negation 
regexnegation = r'[^A-Za-z ]+' # ^ means negation not A to Z or a to z, no spaces
matchesnegation = re.findall(regexnegation, strwithnums)
print(matchesnegation)

# Excercises: Level 1
# 1. Most frequent word in the following paragraph
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regexsplit = r' '
strwithoutperiod = re.sub('\.','',paragraph)
print(strwithoutperiod)

eachword = re.split(regexsplit, strwithoutperiod)

eachuniqueword = set(eachword)

eachuniquewordcount = []
eachuniquewordcountlst = []
for word in eachuniqueword:
    i  = 0
    for each in eachword:
        if word == each:
            i += 1
    eachuniquewordcount.append(i)
    eachuniquewordcountlst.append(word)

zipped = zip(eachuniquewordcountlst, eachuniquewordcount)
res = sorted(zipped, key = lambda x: x[1], reverse = True)

for key in res:
    print(key)

# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
exertxt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regexexer = r'[-| ]\d+'
txtnums = re.findall(regexexer,exertxt)
inttxtnums =[]
for num in txtnums:
    intnums = int(num)
    inttxtnums.append(intnums)
print(inttxtnums)
minfarthestpoint = min(inttxtnums)
maxfarthestpoint = max(inttxtnums)
diff = maxfarthestpoint - minfarthestpoint
print('Distance: ',diff)

# Exercise: level 2: Write a pattern which identifies if a string is a valid python variable
def isvalidpythonvarname(varname):
    return bool(re.search(r'^[_a-z]\w*$',varname))
print(isvalidpythonvarname('firstname'))  
