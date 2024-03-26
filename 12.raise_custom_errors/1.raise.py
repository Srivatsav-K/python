n = int(input('Enter a number between 5 and 11'))

if (n < 5 or n > 11):
    raise ValueError('Value should be between 5 and 11')
else:
    print(n)


# Quick task : do not raise an error if 'quit' is typed. Else thow an error.
value = input('Enter a number between 5 and 10 :')

if (value.strip() == 'quit'):
    print('Execution exited')
else:
    try:
        n = int(value)
        if (n < 5 or n > 10):
            raise ValueError('Value should be between 5 and 10')
        else:
            print(n)
    except Exception as e:
        print(e)
