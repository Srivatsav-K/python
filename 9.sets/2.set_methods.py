s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}

# union
print('union : ', s1.union(s2))  # {1, 2, 3, 5, 6, 7}
# original sets wont get updated with the union
print(f's1 : {s1} \ns2 : {s2}')
# update sets --> Update a set with the union of itself and others.
s1.update(s2)
print('update', s1)  # {1, 2, 3, 5, 6, 7}

# intersection
cities1 = {"Delhi, jaipur, Chandigarh", "Mumbai"}
cities2 = {"Chennai", "Bangalore", "Hyderabad", "Mumbai"}
print('s1 intersection s2 : ', cities1.intersection(cities2))  # {'Mumbai'}
# intersection_update --> Update a set with the intersection of itself and another.
cities1.intersection_update(cities2)
print('intersection_update : ', cities1)

# symmetric difference = (A union B) - (A intersection B)
n1 = {1, 2, 3, 4, 5}
n2 = {4, 5, 6, 7, 8}
# {1, 2, 3, 6, 7, 8}
print('symmetric_difference', n1.symmetric_difference(n2))
# symmetric_difference_update --> Update a set with the symmetric difference of itself and another.
n1.symmetric_difference_update(n2)
print('symmetric_difference_update', n1)  # {1, 2, 3, 6, 7, 8}

# difference --> (A-B) all elements that are in this set but not the others.
num1 = {1, 2, 3, 4, 5}
num2 = {4, 5, 6, 7, 8}
print(num1.difference(num2))  # {1, 2, 3}
# difference_update -->Remove all elements of another set from this set.
num1.difference_update(num2)
print('difference_update', num1)  # {1, 2, 3}
