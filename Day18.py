# Regular Expressions: It is a special text string that helps find patterns in data
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
# re.findall(): returns a list containing all matches
# re.split(): takes a string, splits it at the match points, returns a list
# re.sub(): replaces one or many matches with a string

