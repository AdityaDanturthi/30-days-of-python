# Regular Expressions: It is a special text string that helps find patterns in data
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
