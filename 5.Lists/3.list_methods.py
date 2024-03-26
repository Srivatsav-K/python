lst1 = [12, 1, 65, 8, 5, 3]

# append
lst1.append(20)
print('append', lst1)  # [12, 1, 65, 8, 5, 3, 20, 'sri']
# returns None --> print(lst1.append("sri"))  # None

# pop
lst1.pop()
print('pop', lst1)
lst1.pop(3)
print('pop element at index 3', lst1)

# insert
lst1.insert(1, 200)
print('insert', lst1)

# remove : Remove first occurrence of value. Raises ValueError if the value is not present.
lst1.remove(5)
print('remove', lst1)
# lst1.remove(10)  # ValueError: list.remove(x): x not in list

# sort ascending order
lst1.sort()  # Sort the list in ascending order and return None.
print('sort a-z', lst1)  # [1, 3, 5, 8, 12, 20, 65]

# sort descending order
lst1.sort(reverse=True)
print('sort z-a', lst1)  # [65, 20, 12, 8, 5, 3, 1]

# sort strings
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print("sorted strings", colors)  # ['blue', 'green', 'indigo', 'voilet']

# reverse
lst1.reverse()
print('reverse', lst1)

# index --> Return first index of value.
# print(lst1.index(10))  # ValueError: 10 is not in list
print('indexOf', lst1.index(65))  # 6

# count --> Return number of occurrences of value.
print('count', lst1.count(3))  # 1

# copy -> deep copy
a = [1, 2]
b = a.copy()
b[0] = 10
print('original', a)
print('copy', b)

# concatenation
c = [10, "sri"]
d = ["vatsav", 1]
print('concatenation', c+d)  # [10, 'sri', 'vatsav', 1]

# extend
e = [1, 2]
e.extend([3, 4, 5, 6, 7, 8, 9])
print('extend', e)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
