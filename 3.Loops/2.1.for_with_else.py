for i in []:
    print(i)
else:
    print('Print when condition fails')


for i in range(6):
    print(i)
    if (i == 4):
        break
else:
    print('else block wont get executed since break keyword is used. break means execution of for loop is successfully exited')


for i in range(5):
    print(f'iteration no {i+1} in for loop')
else:
    print('else block in loop')
print('out of loop')
