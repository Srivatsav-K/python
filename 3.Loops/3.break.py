for i in range(15):
    if (i == 10):
        print('End the loop')
        break

    print(f'5 X {i+1} = {5*(i+1)} ')


for i in range(1, 101, 1):
    print(i, end=' ')

    if (i == 50):
        break
    else:
        print('Mississippi')

print('Thank you')
