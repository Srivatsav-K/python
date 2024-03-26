# Dictionaries are ordered in python version 3.7 onwards

details = {
    'name': 'Sri',
    'age': 23,
    'isStudent': True
}

print(details)

# accessing values in a dictionary
# Difference -> .get() does not throw error
# to access number keys, for example : details[2] and not details ['2']
print(details['age'])  # 23
print(details.get('name'))  # Sri

# keys()
keys = details.keys()
print(type(keys))  # < class 'dict_keys' >
print(keys)  # dict_keys(['name', 'age', 'isStudent'])

for key in keys:
    print('getting values from a array of keys :', details[key])

# values()
print(details.values())  # dict_values(['Sri', 23, True])

# items()
# dict_items([('name', 'Sri'), ('age', 23), ('isStudent', True)])
items = details.items()
print(items)

for key, value in items:
    print('key :', key)
    print('value :', value)
