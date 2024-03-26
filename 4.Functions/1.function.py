def calculateGmean(numbers):
    length = len(numbers)
    sum = 0

    for i in numbers:
        sum += i

    return sum/length


print(calculateGmean([1, 2, 3, 4]))  # 2.5


def completeLater(a, b):
    pass


print(completeLater(1, 2))  # None


def geaterNum(a, b):
    if (a > b):
        return a

    return b


print(geaterNum(1, 2))  # 2
