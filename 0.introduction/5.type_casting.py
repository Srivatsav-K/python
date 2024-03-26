# Type casting  int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict()

# EXPLICIT TYPECASTING

a = '1'
b = '2'
print(a+b)  # string concatenation --> '12'

c = '2'
d = '5'
print(int(c)+int(d))  # 6

e = 'sri'
f = '2'
# print(int(e)+int(f))  # ValueError: invalid literal for int() with base 10: 'sri'

print(float('2'))  # 2.0
print(ord('s'))  # Return the Unicode code point for a one-character string --> 115
print(hex(2))  # Return the hexadecimal representation of an integer --> 0x2
print(oct(2))  # Return the octal representation of an integer -->0o2
# Built-in immutable sequence.
# If no argument is given, the constructor returns an empty tuple. If iterable is specified the tuple is initialized from iterable's items.
# If the argument is a tuple, the return value is the same object.
print(tuple((1, 2, [5, 6], 'sri')))
print(list((1, 2, 3)))
print(dict())


# IMPLICIT TYPECASTING

g = 30
h = 11.0

print(type(g))  # <class 'int'> implicitly converts the data type of g to int
print(type(h))  # <class 'float'> implicitly converts the data type of h to float

# 41.0, <class 'float'> implicitly converts the result to float as it is a float addition
print(g+h, type(g+h))
