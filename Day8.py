# Dictionaries

# Creating a dictionary
emptyDict = {}

dct = {'Name':'Aditya Danturthi',
        'Age': 260,
        'skills':['JavaScript', 'Tableau', 'Power BI', 'SQL', 'Python'],
        'address':{
            'street':'this street',
            'zipcode':'A1BC2D'
        }
}

# Dictionary length
print(len(dct)) # Prints number of key value pairs

# Accessing items in a dictionary
print(dct['Name']) # Aditya Danturthi
print(dct['skills'][4]) # Python
print(dct['address']['zipcode']) # A1BC2D

# Adding items to a dictionary
dct['skills'].append('scikit-learn')

# Modifying items in a dictionary
dct['age'] = 262

# Checking keys in a dictionary
print('address' in dct) # True

# Removing key-value pairs from a dictionary
dct.pop('age') # removes age from dictionary
dct.popitem() # removes address from dictionary
del dct['Name'] # removes name from dictionary

# Clearing dictionary
print(dct.clear()) # removes all items from dictionary

# Deleting dictionary
del dct

dct = {'Name':'Aditya Danturthi',
        'Age': 260,
        'skills':['JavaScript', 'Tableau', 'Power BI', 'SQL', 'Python'],
        'address':{
            'street':'this street',
            'zipcode':'A1BC2D'
        }
}

# Copying a dcitionary
dct_copy = dct.copy()

# Getting dictionary keys as a list
dctkeys = dct.keys()
print(dctkeys)

# Getting dictionary values as a list
dctvalues = dct.values()
print(dctvalues)

# Exercises: Day 8

# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog = {'name':'Tom', 'breed': 'Newfie', 'age': 1}
print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'firstname':'', 'lastname':'','gender':'', 'maritalStatus':'', 'skills':'', 'country':''
    , 'city':'', 'address':''}

# Get the length of the student dictionary
print(len(student))
