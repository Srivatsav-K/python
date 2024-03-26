# VARIABLES AND DATA TYPES

A = 22  # <class 'int'>
B = 'Hello world'  # <class 'str'>
C = True  # <class 'bool'>
D = None  # <class 'NoneType'>
E = complex(8, 2)

# type()
print(type(E))  # <class 'complex'>

# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(A+B)


# Data Types

# Number
INTEGER_NUMBER = 10
FLOAT_NUMBER = 2.05
COMPLEX_NUMBER = 2+5j

# String
STRING = 'string data type'

# Boolean
BOOLEAN = False


# List : A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets. Lists are mutable and can be modified after creation.
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1, type(list1))

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"), 3)
print(tuple1, type(tuple1))

# dict : A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1, type(dict1))
