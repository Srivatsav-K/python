price_of_apple = 61
budget = 50

if (price_of_apple <= budget):
    print('Alexa, add apple to shopping list')
elif ((price_of_apple > budget) and (price_of_apple <= (budget+10))):
    print('Alexa, add apples to wishlist')
else:
    print('Alexa, do not add apple to shopping list')

# nested if else
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
