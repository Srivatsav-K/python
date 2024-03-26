str = 'hey how are you'

arr = ['Apple', 'Mango', 'Kiwi']

for i in str:
    print(i)

for i in arr:
    print(i)

# range(stopIndex)
for i in range(5):
    print(i)  # prints 0-4

print('\n')

# range(startIndex,stopIndex,increment/decrement)
for i in range(3, 0, -1):  # prints-> 3->1
    print(i)
