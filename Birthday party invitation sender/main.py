#Mail Merge

with open("./invitees.txt") as invitees:
    invite_list = invitees.readlines()

with open("./starting_letter.txt") as base:
    base_letter = base.read()
    
for name in invite_list:
    with open(f"./letter_for_{name.strip()}.txt", mode = "w") as letter:
        letter.write(base_letter.replace("[name]", name.strip()))
        
#Running this code will create as many letters as there are the number of invitees with each letter written for a specific invitee
#You can add more invitees to invitees.txt
#The starting_letter.txt contains the base letter for all
#What it does is that it changes the name in the base letter for every invitee

