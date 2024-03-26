name = 'sri'
greet_msg = "Hey"

# formatted strings
statement1 = f'He said, "{greet_msg}, {name}"'
print(statement1)  # He said, "Hey, sri"

# Use quotes inside string
statement2 = "He said,\"Hello\""
print(statement2)  # He said,"Hello"

# New line escape sequence
print('This is an escape sequence. \nIt is used for a sentence to span over 2 lines.')

# raw strings
print(r'Esacpe sequences such as \n will have no effect here')

multi_line_string = '''Muhammad Ali's quote reads as follows:
"Float like a butterfly,
Sting like a bee"'''
print(multi_line_string)


print(name[0])

for character in name:
    print(character)
