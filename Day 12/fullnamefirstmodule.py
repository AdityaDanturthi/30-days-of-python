def fullname(firstname, lastname):
    name = firstname+' '+lastname
    return name

def addtwonumbers(*nums):
    total =0
    for i in nums:
        total += i
    return total