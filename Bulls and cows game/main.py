#Bulls and Cows game

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

import random
from art import *

def generate_random():
    secret = ''
    while len(secret) != 4:
        no = random.randint(0, 9)
        flag = True
        for i in secret:
            if int(i) == no:
                flag = False
        if flag:
            secret += str(no)
    return secret

def bulls_and_cows(num, secret):
    bulls = 0
    cows = 0
    total = 0
    if num == secret:
        print("You win!")
        print(f"The number was indeed {num}.")
        return 0
    else:
        for i in range(4):
            if num[i] == secret[i]:
                bulls += 1
        for i in secret:
            if i in num:
                total += 1
        cows = total - bulls
    print(f"{bulls}B{cows}C")

print("========================================================================================")
print(text2art("Bulls      and      Cows"))
end = False
random_no = generate_random()
while not end:
    guess = input("\nMake a guess: ")
    if len(guess) != 4:
        print("\nGuess a 4-digit number.")
        break
    if bulls_and_cows(guess, random_no) == 0:
        end = True
