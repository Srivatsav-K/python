# Available from python 3.6

# Old way 1
str1 = 'My name is {} and I am from {}'
# format method replaces the the empty braces with values in sequential order of the arguments provided.
# My name is Srivatsav and I am from Chennai
print(str1.format('Sri', 'Chennai'))

# Drawback
print(str1.format("Chennai", "Sri"))  # My name is Chennai and I am from Sri.

# Old way 2 -> provide indexes in the empty braces
str2 = "My name is {1} and I am from {0}"
# My name is Srivatsav and I am from Chennai
print(str2.format("Chennai", "Srivatsav"))

# f strings
name = 'Srivatsav'
age = 23
print(f'My name is {name}. I am {age} years old')


# Limit decimal places
num = 12.32424
print(format(num, ".3f"))

txt = "For {price:.2f} only"
print(txt.format(price=99.87198728))  # named parameter

print(f'{num:.2f}')


# Retain f string as f string (Do not interpolate variables)
name = 'Sri'
print(f'My name is {{name}}')  # My name is {name}
