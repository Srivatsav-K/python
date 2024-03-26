# TUPLES ARE IMMUTABLE

# In python we cannot create a tuple with single element. It will take the type of the element directly.
tup = (1)
print(type(tup), tup)  # <class 'int'> 1

# To create a tuple with a single element:
tup1 = (1,)
print('Tuple with single element', tup1)

# Tuple cannot be modified
# tup[0] = 12  # 'tup' does not support item assignment

# access element in a tuple
tup = (0, 1, 2, 3, 4, 5)
print(tup[3])  # 3
print(tup[-3])  # negative index ->  tup[len(tup)-3] -> 3
# print(tup[34])  # IndexError: tuple index out of range


# slice -> returns a new sliced tuple. Does not modify the original
tup2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
tup[:4]
tup3 = tup2[:4]
print(tup3)  # (0, 1, 2, 3)
print(tup2)  # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# list slice
lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst1[:4]
lst2 = lst1[:4]
print(lst2)
print(lst1)
