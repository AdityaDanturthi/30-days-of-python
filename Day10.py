# Loops

# While loop
count= 0
while count < 5:
    print(count)
    count += 1
else:
    print(count)

# break and continue
count = 0
while count < 5:
    print(count) # print 0, 1, 2
    count += 1
    if count == 3:
        break

count = 0
while count < 5:
    print(count) # print 0, 1, 2, 4 (skips 3)
    count += 1
    if count == 3:
        continue
    print(count)
    count += 1