# Higher order functions

# Function as a parameter
def addnums(nums): # regular function
    return sum(nums) # in-built sum function

def higherorderfunction(f, lst): # function as a parameter
    total = f(lst)
    return total

result = higherorderfunction(addnums, [1, 2, 3, 4, 5])
print(result)