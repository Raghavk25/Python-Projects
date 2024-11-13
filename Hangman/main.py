#Hangman

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from art import *
from replit import clear
from random_word import RandomWords
stages = ['''             +---+
             |   |
                 |
                 |
                 |
                 |
          ===========''', 
          '''             +---+
             |   |
             O   |
                 |
                 |
                 |
          ===========''',
          '''             +---+
             |   |
             O   |
             |   |
                 |
                 |
          ===========''',
          '''             +---+
             |   |
             O   |
            /|   |
                 |
                 |
          ===========''',
          '''             +---+
             |   |
             O   |
            /|\  |
                 |
                 |
          ===========''',
          '''             +---+
             |   |
             O   |
            /|\  |
            /    |
                 |
          ===========''',
          '''             +---+
             |   |
             O   |
            /|\  |
            / \  |
                 |
          ===========''']
print("=========================================================================")
print(text2art("Hangman"))
print("Here are the rules: ")
print("1. You have to guess the word letter by letter.")
print("2. If you guess a right letter, it fills in the blank(s).")
print("3. If you guess a wrong letter, you lose a life.")
print("4. If you guess the word correctly before the man hangs, you win.")
print("5. If you don't guess the word correctly before the man hangs, you lose.")
print("6. For repetition of a wrong letter, you lose lives.")
print("7. For repetition of a right letter, you lose no lives.")
print("=========================================================================")

def play_game():
    r = RandomWords()
    word = r.get_random_word()
    display = []
    for i in word:
        display += "_"
    print(f"Word = {' '.join(display)}\n")
    print(stages[0])
    
    end = False
    lives = 0
    while not end:
        guess = input("\n\nGuess a letter: ").lower()
        if guess in display:
            print(f"\nYou have already guessed {guess}.\n")
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = word[i]
        if guess not in word:
            lives += 1
            print(f"\nYou guessed the letter {guess}. That's not in the word. You lose a life.\n")
            print(stages[lives])
            if lives == 6:
                end = True
                print("\nYou lose!")
                print(f"The word was {word}")
                print("=========================================================================")
                break
        if guess in word:
            print(stages[lives])
        print(f"Word = {' '.join(display)}")
        if "_" not in display:
            end = True
            print("\nYou win!")
            print("=========================================================================")
end1 = False
while not end1:
    play_again = input("\nDo you want to play a game of Hangman? Type 'y' for yes or 'n' for no.\n").lower()
    if play_again == "n":
        print("\nGoodbye!")
        end1 = True
    elif play_again == "y":
        clear()
        play_game()
    else:
        print("\nInvalid input.")
        end1 = True



