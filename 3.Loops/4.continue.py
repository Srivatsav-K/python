# continue is used to skip the iteration

# Print 8 table till 15, but do not print 8*10
for i in range(1, 15, 1):
    if (i == 10):
        print('Skip the iteration 8 * 10 = 80')
        continue
    else:
        print(f'8 * {i} = {8*i}')

# Print even numbers
arr = [1, 2, 3, 4, 5, 6]

for i in arr:
    if (i % 2 != 0):
        continue
    else:
        print(i)
