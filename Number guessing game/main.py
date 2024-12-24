#Number Guessing Game

import random
from art import *
print("=====================================================================================================================================")
print("Welcome to the number guessing game!")
print(text2art("Number     Guessing      Game"))
print("\nI am thinking of a number from 1 to 100. Guess it.")
number = random.randint(1, 100)
difficulty = input("Choose a difficulty level. Type 'E' for easy, 'M' for medium, or 'H' for hard.\n").upper()
valid = True
if difficulty == 'E':
    attempts = 10
elif difficulty == 'M':
    attempts = 7
elif difficulty == 'H':
    attempts = 5
else:
    print("\nInvalid input.")
    valid = False
if valid:
    print(f"You will get {attempts} attempts to guess the number.\n")
    guessed = False
    for i in range(attempts):
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print(f"\nYou have got it!.\nThe number was indeed {number}.")
            guessed = True
            break
        if attempts - i - 1 != 0:
            print("Guess again.")
            print(f"You have {attempts-i-1} remaining attempt(s) to guess.\n")
    if guessed == False:
        print("\nYou have run out of attempts. You lose!")
        print(f"The number was {number}.")
print("=====================================================================================================================================")
