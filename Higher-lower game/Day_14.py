#The Higher Lower Game

import random
from art import *
from replit import clear
print("=================================")
print("Welcome to the Higher Lower game!")
print(text2art("""Higher
Lower"""))
accounts = [{"Name": "Cristiano Ronaldo", "Count": 635}, {"Name": "Jennifer Lopez", "Count": 252}, {"Name": "Rihanna", "Count": 151}, 
            {"Name": "Neymar", "Count": 223}, {"Name": "Instagram", "Count": 674}, {"Name": "Dwayne Johnson", "Count" : 396}, 
            {"Name": "Beyoncé", "Count": 317}, {"Name": "Lionel Messi", "Count":  504}, {"Name": "Ariana Grande", "Count":  378},
            {"Name": "Virat Kohli", "Count":  270}, {"Name": "Miley Cyrus", "Count":  215}, {"Name": "Drake", "Count":  145}, 
            {"Name": "Selena Gomez", "Count":  426}, {"Name": "Taylor Swift", "Count":  283}, {"Name": "Chris Hemsworth", "Count":  59.3},
            {"Name": "Nicki Minaj", "Count":  228}, {"Name": "Priyanka Chopra", "Count":  91.6}, {"Name":  "Dua Lipa", "Count":  88}, 
            {"Name": "Cardi B", "Count":  166}, {"Name": "Chris Brown", "Count":  145},{"Name": "Akshay Kumar", "Count":  67.7},
            {"Name": "Leonardo DiCaprio", "Count": 62}, {"Name": "Johnny Depp", "Count": 29}, {"Name": "Julia Roberts", "Count": 13},
            {"Name": "Cameron Diaz", "Count": 12}, {"Name": "Jamie Foxx", "Count": 17}, {"Name": "Emma Watson", "Count": 75},
            {"Name": "Rafael Nadal", "Count": 21}, {"Name": "Maria Sharapova", "Count": 5}, {"Name": "Robert Downey Jr.", "Count": 56},
            {"Name": "Amitabh Bachchan", "Count": 38}, {"Name": "Ed Sheeran", "Count": 48}, {"Name": "Shawn Mendes", "Count": 72},
            {"Name": "Jeff Bezos", "Count": 4}, {"Name": "Bill Gates", "Count": 11}, {"Name": "Lady Gaga", "Count": 56},
            {"Name": "Camila Cabello", "Count": 65}, {"Name": "The Weeknd", "Count": 75}, {"Name": "Harry Styles", "Count": 47},
            {"Name": "Shah Rukh Khan", "Count": 47}, {"Name": "John Cena", "Count": 21}, {"Name": "Henry Cavill", "Count": 27},
            {"Name": "Olivia Rodrigo", "Count":  38}, {"Name": "Millie Bobby Brown", "Count":  63}, {"Name": "Zac Efron", "Count": 62},
            {"Name": "Eminem", "Count": 44}, {"Name": "Bella Hadid", "Count": 61.3}, {"Name": "Gigi Hadid", "Count": 78},
            {"Name": "Anushka Sharma", "Count": 68}, {"Name": "MS Dhoni", "Count": 50}, {"Name": "Mark Zuckerberg", "Count": 14},
            {"Name": "Roger Federer", "Count": 13}, {"Name": "Arnold Schwarzenegger", "Count": 26}, {"Name": "Adele", "Count": 57},
            {"Name": "Natalie Portman", "Count": 9}, {"Name": "Charlize Theron", "Count": 8}, {"Name": "Tom Hardy", "Count": 10},
            {"Name": "Oprah Winfrey", "Count": 23}, {"Name": "Michelle Obama", "Count": 57}, {"Name": "Chris Pratt", "Count": 46},
            {"Name": "Anne Hathaway", "Count": 34}, {"Name": "Joe Biden", "Count": 19}, {"Name": "Donald Trump", "Count": 26},
            {"Name": "Timothée Chalamet", "Count": 20}, {"Name": "Tom Holland", "Count": 65}, {"Name": "Nicole Kidman", "Count": 10},
            {"Name": "Katy Perry", "Count":  206}, {"Name": "Aishwarya Rai", "Count":  14.2}, {"Name":  "Alia Bhatt", "Count":  85}, 
            {"Name": "Kim Kadarshian", "Count":  362}, {"Name": "Billie Eilish", "Count":  119}, {"Name": "Shakira", "Count":  90.4},
            {"Name": "Vin Diesel", "Count":  102}, {"Name": "Narendra Modi", "Count":  91.2}, {"Name": "Kylian Mbappé", "Count":  120}, 
            {"Name": "David Beckham", "Count":  88.3}, {"Name": "Hrithik Roshan", "Count":  48}, {"Name": "Gal Gadot", "Count":  108}, 
            {"Name": "Zendaya", "Count":  183}, {"Name": "Blake Lively", "Count":  45}, {"Name": "Kevin Hart", "Count":  179}, 
            {"Name": "Barack Obama", "Count": 36}, {"Name": "Rahul Gandhi", "Count": 11}, {"Name": "Novac Djokovic", "Count": 15},
            {"Name": "Demi Lovato", "Count":  155}, {"Name": "Justin Bieber", "Count":  294}, {"Name": "Angelina Jolie", "Count":  15.2},
            {"Name": "Chris Evans", "Count":  17.8}, {"Name": "Kylie Jennar", "Count":  398}, {"Name": "Khloé Kardashian", "Count":  308}, 
            {"Name": "Kendall Jenner", "Count":  292}, {"Name": "Jennifer Anniston", "Count":  44.9}, {"Name": "Shraddha Kapoor", "Count":  90.4}, 
            {"Name": "Ellen DeGeneres", "Count":  138}, {"Name": "LeBron James", "Count":  159}, {"Name": "Kourtney Kardashian", "Count":  222},
            {"Name": "Snoop Dogg", "Count":  87.5}, {"Name": "Ryan Reynolds", "Count":  52}, {"Name": "Hugh Jackman", "Count":  32}, 
            {"Name": "Jenna Ortega", "Count":  38}, {"Name": "Tom Cruise", "Count": 12}]

print("\nWho has more Instagram followers?\n")
A = random.choice(accounts)
score = 0
def play_game():
    global A  #global keyword indicates that global variable is being manipulated.
    global score
    print(f"Option A: {A["Name"]}")
    print("OR")
    B = random.choice(accounts)
    while A == B:
        B = random.choice(accounts)
    print(f"Option B: {B["Name"]}\n")
    choice = input("Type 'A' or 'B'.\n").upper()
    if choice == "A":
        if A["Count"] >= B["Count"]:
            clear()
            score += 1
            print(f"\nThat's right! Current score: {score}\n")
            A = B
            play_game()
        else:
            print("\nOops, you lose.")
            print(f"Your score: {score}")
    elif choice == "B":
        if B["Count"] >= A["Count"]:
            clear()
            score += 1
            print(f"\nThat's right! Current score: {score}\n")
            A = B
            play_game()
        else:
            print("\nOops, you lose.")
            print(f"Your score: {score}")
    else:
        print("\nInvalid choice!")
        print(f"Your score: {score}")
play_game()







