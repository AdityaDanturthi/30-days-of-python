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