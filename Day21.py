# Classes and Objects

# Creating a class
class Person:
    pass
print(Person)

# Creating an object
p = Person()
print(p)

# Class constructor
class Person:
    def __init__(self, name): # self allows to add a parameter to a class
        self.name = name

p = Person('Aditya')
print(p.name)
print(p)

# Adding more parameters to the constructor
class Person:
    def __init__(self, name, province, age): # self allows to add a parameter to a class
        self.name = name
        self.province = province
        self.age = age

p = Person('Aditya', 'NL', 260)
print(f' Hi %s from %s of age %d' %(p.name,p.province,p.age))
print(p)


