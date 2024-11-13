#Mail Merge

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

with open("Bootcamp python//2. Intermediate level//Day_24//invitees.txt") as invitees:
    invite_list = invitees.readlines()

with open("Bootcamp python//2. Intermediate level//Day_24//starting_letter.txt") as base:
    base_letter = base.read()
    
for name in invite_list:
    with open(f"Bootcamp python//2. Intermediate level//Day_24//letter_for_{name.strip()}.txt", mode = "w") as letter:
        letter.write(base_letter.replace("[name]", name.strip()))
        
#Running this code will create as many letter as there are the number of invitees with each letter written for a specific invitee
#You can add more invitees to invitees.txt
#The starting_letter.txt contains the base letter for all
#What it does is that it changes the name in the base letter for every invitee

