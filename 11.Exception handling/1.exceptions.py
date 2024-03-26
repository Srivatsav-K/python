try:
    num = int(input('Enter a number'))
    print(num % 2)
except Exception as e:
    print('Error : ', e)  # Error:  invalid literal for int() with base 10: 'sri'


try:
    num = int(input('Enter the index : '))
    arr = [6, 5]
    print(arr[num])
except ValueError as v:
    # Value error :  invalid literal for int() with base 10: 'ssri'
    print('Value error : ', v)
except IndexError as i:
    print('Index error : ', i)  # Index error :  list index out of range
