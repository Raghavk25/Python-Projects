#Blackjack 

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

import random
from replit import clear
from art import *
print(text2art("Blackjack"))

def deal_cards():
    """Deals the cards."""
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Takes a list of cards and returns the score calculated from the cards."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, dealer_score):
    """Compares the scores of the user and the dealer."""
    if user_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "You lose! The dealer has a blackjack."
    elif user_score == 0:
        return "You win! You have a blackjack."
    elif user_score > 21:
        return "You lose! You went over."
    elif dealer_score > 21:
        return "You win! The dealer went over."
    elif user_score > dealer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    game_over = False
    user_cards = []
    dealer_cards = []
    for i in range(2):
        user_cards.append(deal_cards())
        dealer_cards.append(deal_cards())
    while not game_over:   #This while loop is for the user to keep drawing cards as long as they wish.
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {user_cards}. Your score: {user_score}")
        print(f"Dealer's first card: {dealer_cards[0]}")
        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_more = input("Type y to get another card. Type n to pass.\n").lower()
            if draw_more == "y":
                user_cards.append(deal_cards())
            else:
                game_over = True
    while dealer_score != 0 and dealer_score < 17:   #This while loop is for the dealer to keep drawing cards as long as the sum is under 17.
        dealer_cards.append(deal_cards())
        dealer_score = calculate_score(dealer_cards)
    print(f"\nYour final hand: {user_cards}. Your final score : {user_score}")
    print(f"Dealer's final hand: {dealer_cards}. Dealer's final score : {dealer_score}")
    print(compare(user_score, dealer_score))
    print("===========================================================================")

end1 = False
while not end1:
    play_again = input("\nDo you want to play a game of Blackjack? Type 'y' for yes or 'n' for no.\n").lower()
    if play_again == "y":
        clear()
        play_game()
    elif play_again == "n":
        print("\nGoodbye!")
        end1 = True
    else:
        print("\nInvalid input.")
        end1 = True



