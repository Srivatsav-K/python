# Take parameters as a tuple(immutable array)
def average(*numbers):  # * parameters are taken as a tuple

    print(type(numbers))
    print(numbers[0])

    sum = 0
    total_numbers = len(numbers)

    for i in numbers:
        sum += i

    return sum/total_numbers


print(average(1, 2, 3, 4, 5))


# Take parameters as dictionary(object)
def personal_details(**details):
    print(type(details), details)
    return f'{details["name"]} is {details["age"]} years old and lives in {details["city"]} '


print(personal_details(name='Sri', age=22, city='Chennai'))
