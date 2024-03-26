def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return n*factorial(n-1)


# Driver code
num = 4
print(f'factorial of {num} is :', factorial(num))


# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * 1


def fibonacci(n):
    '''returns fibonacci series till n.
        f0 = 0
        f1 = 1
        f2 = f1+f0

        fn = fn-1 + fn-2
    '''
    if (n == 0 or n == 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(12))
