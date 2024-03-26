fruits = ('Apple', "mango", "orange", "banana")

# len
print(len(fruits))

# count
tup1 = (1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 7)
print(tup1.count(2))  # 2

# index  -> returns the first occurance index of the value. Throws Value error if not present.
tup2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print('indexOf "3" : ', tup2.index(3))
print("indexOf 3 iafter slicing 2 to 5 :", tup2.index(3, 3, 8))
