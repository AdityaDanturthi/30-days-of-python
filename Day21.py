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

# Object methods: Objects can have methods. Methods are functions which belong to an object.
class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.province = args[1]
        self.age = args[2]
    def details(self): 
        return f'Hi {self.name} from {self.province} of age {self.age}'

p = Person('Aditya','NL',260)
print(p.details())

# Default values during instantiation to avoid errors when object is called without passing parameters
class Person:
    def __init__(self, name = 'Aditya', province = 'NL', age = 260):
        self.name = name
        self.province = province
        self.age = age
    def details(self):
        return f'Hi {self.name} from {self.province} of age {self.age}'

p1 = Person()
print(p1.details())
p2 = Person('Alex', 'QC', 260)
print(p2.details())

# Method to modify default class values
class Person:
    def __init__(self, name = 'Aditya', province = 'NL', age = 260) :
        self.name = name
        self.province = province
        self.age = age
        self.skills = []
    
    def details(self):
        return f'Hi {self.name} from {self.province} of age {self.age}'

    def addskills(self,skill):
        self.skills.append(skill)
    
    def detailswithskills(self):
        skillstr = ''
        for i in self.skills:
            skillstr += i+', '    
        skillstr = skillstr[:-2]
        return f'Hi {self.name} from {self.province} of age {self.age} is skilled in {skillstr}'

p1 = Person()
p1.addskills('Javascript')
p1.addskills('Python')
p1.addskills('C')
p1.addskills('Java')
#print(p1.details)
print(p1.detailswithskills())

p2 = Person('Alex', 'QC', 260)
#print(p2.details())
p2.addskills('Numpy')
print(p2.detailswithskills())
