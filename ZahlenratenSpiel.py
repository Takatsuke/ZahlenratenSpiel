'''
This program lets you guess a number between 0 and 100. Only whole numbers are used.
'''
import random

sought = random.randint(0,100)

try:
    x = input("Please guess which number is sought. The number you are looking for is between 0 and 100: ")

    while int(x) != sought:
        if int(x) < sought:
            x = input("The indicated number is too small. Please try again: ")
        else:
            x = input("The indicated number is too large. Please try again: ")

    print(f"Congratulations! You've Found the right number! It was {sought}")
except:
    print("Your input does not meet the expected format. Please use only whole numbers.")

