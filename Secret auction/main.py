#Secret Auction Program

from replit import clear
from art import *
def find_highest(bids):
    max = 0
    tie = 0
    for i in bids:
        if bids[i] > max:
            max = bids[i]
            max_bidder = i
    for i in bids:
        if bids[i] == max:
            print(f"The winner is {i} with a bid of {max}.")
            tie += 1
            if tie > 1:
                print("Have a go again to break the tie.")
                print("=====================================================")
bids = {}
end = False
print("=====================================================")
print("Welcome to secret bid program!")
print(text2art("Secret       Bid       Program"))
while not end:
    name = input("\nEnter your name: ")
    bid = int(input("Enter your bid: $"))
    bids[name] = bid
    other = input("Are there any other bids? Type 'y' for yes or 'n' for no.\n").lower()
    clear()
    if other == "n":
        find_highest(bids)
        end = True
    elif other == "y":
        pass
    else:
        print("\nInvalid input.")
        end = True



