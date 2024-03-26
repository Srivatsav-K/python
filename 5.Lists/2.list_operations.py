details = [22, "sri", ["Chennai", "Bangalore"]]

# in
print(["Chennai", "Banglaore"] in details)  # False
print("sri" in details)  # True

# len
print(len(details))  # 3

# slice
print(details[:])
print(details[:2])  # [22, 'sri']
print(details[:-2])  # details[0:1]

# jump index -> slice the list in steps of mentioned step(3rd argument)
# syntax -> [startIndex : stopIndex : jumpIndex]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# slices the list from 0->5 by choosing every 3rd element --> [0,3]
print(numbers[0:6:3])


# list comperehension -> generate list on the fly
# syntax --> [ variable for_loop condition ]
lst1 = [i for i in range(10)]
print(lst1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

lst2 = [i+2 for i in range(10)]
print(lst2)  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

lst3 = [i for i in range(10) if i % 2 == 0]
print(lst3)  # [0, 2, 4, 6, 8]

lst4 = list(range(10))
print(lst4)

animals = ["cat", "dog", "bat", "mouse",
           "pig", "horse", "donkey", "goat", "cow"]
print(animals[1:8:3])  # ['dog', 'pig', 'goat']


# EXERCISE
# 1. Accept items which have more than 4 letters in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
result1 = [i for i in names if len(i) > 4]
print(result1)  # ['Sarah', 'Bruno', 'Anastasia']

# 2 .Accept items with the small letter “o” in the new list
result2 = [i for i in names if "o" in i]
print(result2)  # ['Milo', 'Bruno', 'Rosa']
