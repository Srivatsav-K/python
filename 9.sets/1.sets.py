# Sets are unordered collection of data items. They store multiple items in a single variable.

# Set items are separated by commas and enclosed within curly brackets {}.

# Sets are unchangeable, meaning you cannot change items of the set once created.

# Sets do not contain duplicate items.

s = {1, 2, 2, 3, 4, 5, 5}
print(s)  # {1, 2, 3, 4, 5}

s1 = {"Carla", 19, False, 10.5}
print(s1)  # {False, 10.5, 19, 'Carla'}

# Empty Set
print('Type of {} : ', type({}))  # dict
# To create an empty set
s2 = set()
print('Empty set : ', s2)  # set()
print('Type of empty set : ', type(s2))  # <class 'set'>

# Looping over sets
for value in s1:
    # order is not maintained since set is unordered
    print('Looping over a set :', value)

# Empty tuple
t2 = tuple()
print('Type of a tuple with 1 element in a tuple without comma : ', type((1)))  # int
print('empty tuple :', t2)
print('type of empty tuple :', type(t2))
