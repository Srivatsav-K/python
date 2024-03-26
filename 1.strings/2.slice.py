name = 'srivatsav'
# ------0123456789

# slice the entire length of the string
print(name[:])  # 'srivatsav'

# slice a string
print(name[0:3])  # 'sri'
# Adds 0 by default if 1st arg is not provided
print(name[:3])  # 'sri'

# slices till end of the string if 2nd arg is empty
print(name[4:])  # atsav
print(name[-3:])  # sav

# negative index --> [ startIndex : (len(str) - given index)]
print(name[1:-3])  # name[1:(9-3)]--> 'rivat'
print(name[1: len(name)-3])  # name[1:(9-3)]--> 'rivat'

print(name[-1:-3])  # name[len(name)-1:len(name)-3] --> name[8:6] --> ''
print(name[-4:-1])  # --> name[5:8] --> 'tsa'

# length of a string
print(len(name))  # 9

for i in name:
    print(i)
