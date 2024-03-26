# Create a program capable of displaying questions to the user like KBC.
# Use List data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.

import time

name = input('What is your name ? \n').lower()


def greet(name):
    greeting = ''
    hour = int(time.strftime('%H'))

    if (hour >= 16 and hour < 17):
        greeting = 'Good evening'
    elif (hour <= 23):
        greeting = 'Good night'
    else:
        greeting = "Good day"
    return f'{greeting} {name}. Welcome to KBC!'


print(greet(name))

questions = []
