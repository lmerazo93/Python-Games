# ITP 115, Summer 2023
# Lab 3
# Name: Ligia Erazo
# Email: lmerazo@usc.edu
# Section: 31822

import random

random_number = random.randrange(0,51)
print("Computer: I selected a number between 0 and 50 (inclusive).")
print("Guess the number! Enter -1 to quit!")

user_guess =int(input("Guess (enter only numbers): "))
guesses = 1

while user_guess != -1 and user_guess != random_number :
    user_guess = int(input("Guess (enter only numbers): "))
    guesses += 1 #  guesses = guesses + 1

    if user_guess < random_number:
        print("Go higher!")
    elif user_guess > random_number:
        print("Go lower!")


if user_guess == -1:
    print("You lost. The number i guessed was" , random_number)
else:
    print("Great! That is correct")
    print("You guessed the number in" , guesses , "tries.")