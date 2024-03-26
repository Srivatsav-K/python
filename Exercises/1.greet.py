# Create a python program capable of greeting you with Good Morning, Good Afternoon and Good Evening. Your program should use time module to get the current hour. Here is a sample program and documentation link for you:
# https://docs.python.org/3/library/time.html#time.strftime
import time

name = input('Enter your name').title()
print(time.strftime('%H,%M,%S'))

if (int(time.strftime('%H')) < 12):
    print('Good morning', name)
elif (((int(time.strftime('%H')) > 12) and ((int(time.strftime('%H')) < 19)))):
    print('Good evening', name)
else:
    print('Good night', name)
