cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}

# disjoint() --> Return True if two sets have a null intersection.
print('isdisjoint :', cities.isdisjoint(cities2))  # False

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Delhi"}
# issuperset()
print('issuperset :', cities.issuperset(cities2))  # True

# issubset()
print('issubset :', cities2.issubset(cities))  # True

# add() --> Add an element to a set. Has no efffect if element already present
cities2.add('Chennai')
print(cities2)  # {'Chennai', 'Tokyo', 'Delhi'}

# update -->If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
cities2.update({'Bangalore', 'Tokyo'})
print(cities2)  # {'Chennai', 'Delhi', 'Tokyo', 'Bangalore'}

# remove() -->Remove an element from a set; If the element is not a member, raise a KeyError.
cities2.remove('bangalore'.title())
print(cities2)  # {'Delhi', 'Tokyo'}

# discard()
cities2.discard('Chennai')
cities2.discard('mumbai')
print(cities2)  # {'Delhi', 'Tokyo'}

# pop() --> This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered.
popped_element = cities.pop()
print(cities)  # {'Tokyo', 'Berlin', 'Delhi'}
print(popped_element)  # Madrid

# clear() --> This method clears all items in the set and prints an empty set.
cities.clear()
print(cities)  # set()

# del --> del is not a method, rather it is a keyword which deletes the set entirely.
del cities2
print(cities2)  # NameError: name 'cities2' is not defined

# in -->check if an item exists in the set or not.
info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")
