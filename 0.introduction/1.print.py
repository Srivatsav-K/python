# This is a comment in python. A pound symbol is used for comments.

'''
This is a multiline comment in python.
'''

#print statement
print('Hello world')
print('My age is',22)

# seperator
print('My age is',22,sep='~') #My age is~22
print('My age is',22,sep=':') #My age is:22

#end
print('Hello world',end='\n\n')
print('next line')
'''
Hello world

next line
'''

# New line escape sequence
print('This is an escape sequence. \nIt is used for a sentence to span over 2 lines.')
print('''This is also a 
multiline string''')

#raw strings
print(r'Esacpe sequences such as \n will have no effect here')

# Use quotes inside string
print('Taylor\'s version')
print("Taylor's version")


