try:
    index = int(input('Enter the index in the array you want to access : '))
    arr = [1, 2, 3]
    print(arr[index])
except Exception as e:
    print('Exception :', e)
finally:
    print('Code in finally always gets executed irrespective of the outcome of try...except...else blocks')

# # finally exectues even if you return something from a function


def getItem(index):
    try:
        arr = [1, 2, 3]
        return arr[index]
    except IndexError as i:
        print('Index error')
        return i
    print('Print cannot be used as an exception for finally')


print(getItem(10))


def getItem1(index):
    try:
        arr = [1, 2, 3]
        return arr[index]
    except IndexError as i:
        print('Index error')
        return i
    finally:
        print('Executes even when a function returns soemthing')


print(getItem1(10))
