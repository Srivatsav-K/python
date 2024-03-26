details = {
    'name': 'Sri',
    'age': 23,
    'isStudent': True
}

# update() --> The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
additionalDetails = {
    'city': 'Chennai',
    'country': 'India'
}
details.update(additionalDetails)
# {'name': 'Sri', 'age': 23, 'isStudent': True, 'city': 'Chennai', 'country': 'India'}
print(details)

# Removing items from dictionary:
# del
del details['country']
# {'name': 'Sri', 'age': 23, 'isStudent': True, 'city': 'Chennai'}
print(details)

# pop() --> remove specified key and return the corresponding value.If key is not found, default is returned if given, otherwise KeyError is raised
details.pop('city')
print(details)  # {'name': 'Sri', 'age': 23, 'isStudent': True}

# popitem() --> The popitem() method removes the last key-value pair from the dictionary.
details.popitem()
print(details)  # {'name': 'Sri', 'age': 23}
