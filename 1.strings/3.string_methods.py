fact = 'sun rises in the east'

# in
print("rises" in fact)  # True

# Length of a string
print(len(fact))  # 21

# convert the string to upper case
print(fact.upper())  # SUN RISES IN THE EAST
# isupper
print(fact.isupper())

# convert the string to lower case
print(fact.lower())
# islower
print(fact.islower())

# rstrip (right strip) -->Return a copy of the string with trailing whitespace removed. If chars is given and not None, remove characters in chars instead
print('Yeah boiiiiiii '.rstrip())
print('yeah boiiiiii'.rstrip('i'))

# strip
# Return a copy of the string with leading and trailing whitespace removed.
print(' yeah boii '.strip())
print('******Yeah boii******'.strip('*'))

# replace
print('hello world'.replace('hello', 'hey'))
print('one two three one'.replace('one', 'replaced_one', 1))

# split
print('tommy, arthur, john'.split(', '))

# capitalize
# make the first character have upper case and the rest lower case.
print('tHis Is an Unformated sTRing'.capitalize())

# center
# Return a centered string of length width.
# Padding is done using the specified fill character (default is a space).
word = 'Welcome to the console'
print(word.center(50))  # Welcome to the console
# **************Welcome to the console**************
print(word.center(50, '*'))
print(len(word))  # 25
print(len(word.center(50)))  # 50

# count
print('Srivatsav'.count('a'))
print('yes yes yes'.count('yes'))

# endswith
print('Hello world!!!'.endswith('!'))  # True
# slice the string from 5->8 and check if the sliced string endswith the specified string
print('Hello world'.endswith('r', 5, 9))
# True -> Suffix can also be a tuple of strings to try.
print('Hello world'.endswith(('a', 'd', 'c')))

# startswith
print('Hello world!!!'.startswith('H'))  # True
# slice the string from 5,8 and check if the sliced string startswith the specified string
print('Hello world'.startswith(' ', 5, 9))
# True -> Suffix can also be a tuple of strings to try.
print('Hello world'.startswith(('a', 'd', 'c', 'H')))

# find
# Return the lowest index in S where substring sub is found else return -1
print('Srivatsav'.find('v'))  # 3
print('Srivatsav'.find('z'))  # -1

# index
# similar to find but throws an exception if not found
print('Srivatsav'.index('v'))  # 3
# print('Srivatsav'.index('z'))  # ValueError: substring not found

# isalum is alpha numeric
# Return True if the string is an alpha-numeric string A-Z,a-z,0-9, False otherwise.
print('My number is 928119839'.isalnum())  # False (space is present)
print('masJASdn034'.isalnum())  # True

# isalpha
print('asZd'.isalpha())

# isprintable
print('How are you? \n'.isprintable())  # False since '\n' cannot be seen

# isspace : Return True if the string is a whitespace string, False otherwise.
print('   '.isspace())

# title
print('football club barcelona'.title())  # Football Club Barcelona
# istitle
print('football club barcelona'.istitle())  # False

# swapcase
print('Hey How Are You?'.swapcase())  # hEY hOW aRE yOU?
print('sdf sdfs sdf'.title().swapcase())
