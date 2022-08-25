# File Handling

# Opening files for reading
f = open('example.txt')
text = f.read()
print(text)


# Limiting print to first 10 characters
text10 = f.read(10)
print(type(text10))
print(text10)

# readline(): reads only the first one
line = f.readline()
print(type(line))
print(line)

# readlines(): read all the text line by line and returns list of lines
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# splitlines(): another way to get all the lines
splitlines = f.read().splitlines()
print(type(splitlines))
print(splitlines)
f.close()

# Closing a file automatically
with open('example.txt') as f:
    splitlines = f.read().splitlines()
    print(type(splitlines))
    print(splitlines)

# Opening files for writing and appending
with open('example.txt', 'a') as f:
    f.write('This text has to be appended at the end.')

with open('example.txt') as f:
    lines1 = f.read().splitlines()
    print(lines1)

# 'w' creates a new file, if it doesn't exist
with open('writingfileexample.txt', 'w') as f:
    f.write('This will be written in a new file!')

with open('writingfileexample.txt') as f:
    newfile = f.read().splitlines()
    print(newfile)

# Deleting a file
import os
if os.path.exists('p:/c/writingfileexample.txt'):
    os.remove('p:/c/writingfileexample.txt')
    print('Sucessfully deleted!')
else:
    print('File does not exist!')

# File types
# Files with JSON extension: JSON very similar to python dictionary except it is written on a single line

# Python dictionary
DetailsDct = {
    'firstname': 'Aditya',
    'lastname': 'Danturthi',
    'skills': ['Python', 'JavaScript', 'C'],
    'age': 260
}

# JSON
DetailsJSON = "{'firstname': 'Aditya', 'lastname': 'Danturthi', 'skills': ['Python', 'JavaScript', 'C'],'age': 260}"
multilineJSON = '''{
    "firstname": "Aditya",
    "lastname": "Danturthi",
    "skills": ["Python", "JavaScript", "C"],
    "age": 260    
}'''

# Converting JSON to a dictionary
import json
jsontodct = json.loads(multilineJSON)
print(type(jsontodct))
print(jsontodct)
print(jsontodct['firstname'])

# Converting dictionary to JSON
dcttoJSON = json.dumps(DetailsDct, indent=2) 
print(type(dcttoJSON))
print(dcttoJSON)

# Saving as JSON file
with open('example.json', 'w', encoding= 'utf-8') as f:
    json.dump(dcttoJSON, f, ensure_ascii= False, indent= 2)

# File with csv extension
import csv

# with open('P:/c/example.csv', 'w') as f:
#     f.write('Name,Country,Province,Skills')
#     f.write(' Aditya, Canada, Newfoundland, Python')
    

with open('P:/c/example.csv') as f:
    csvreader = csv.reader(f, delimiter=',')
    linecount = 0
    for row in csvreader:
        if linecount == 0:
            print(f'Column names are:{",".join(row)}')
            linecount += 1
        else:
            print(
                f'\t{row[0]} is a programmer. He lives in{row[2]},{row[1]}.')
            linecount += 1
    print(f'Number of lines: {linecount}')

# File with xls extension
import xlrd

excelworkbook = xlrd.open_workbook('example.xls')
print(excelworkbook.nsheets)
print(excelworkbook.sheet_names)

# File with xml extension
import xml.etree.ElementTree as ET
tree = ET.parse('P:/c/example.xml')
root = tree.getroot() # details tag
print('Root tag: ',root.tag)
print('Root attribute: ', root.attrib)
for child in root:
    print('Field: ',child.tag)


