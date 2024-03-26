# while loop
i = 0
while (i < 10):
    print(i)
    i += 1

# Decrementing while loop
count = 20
while (count > 5):
    print(count)
    count = count - 1

# Example
num = int(input('Enter the number'))
while (num != 20):
    num = int(input('Enter the number'))

print('End of while loop')

# while-with-else (code inside while block is executede when while condition fails)
i = 0
while (i < 10):
    print(i)
    i += 1
else:
    print('Printed when condition failed')
