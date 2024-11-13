#Password Manager

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
#messagebox is a module inside tkinter module, so that's why it wasn't imported when we imported all classes from tkinter before

BLACK = "black"
WHITE = "white"
FONT_NAME = "Arial"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', '\\', '[', ']', '{', '}', '<','>', ',', '-', '_', '.']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    password_list = []
    password_list += [random.choice(numbers) for i in range(4)]
    password_list += [random.choice(letters) for i in range(10)]
    password_list += [random.choice(special) for i in range(4)]

    random.shuffle(password_list) #shuffles the items in password_list
    password = ""
    for i in password_list:
        password += i
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = {
        website_entry.get(): {
            "Email": user_entry.get(), 
            "Password": password_entry.get()
        }
    }
    if len(website_entry.get()) == 0 or len(user_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title = "Oops", message = "Please do not leave any fields empty.")
        
    else:
        is_ok = messagebox.askyesno(title = website_entry.get(), message = "Following are the details entered:\n"
                            f"Email/Username: {user_entry.get()}\nPassword: {password_entry.get()}\n"
                            "Do you want to save this entry?")
        if is_ok:
            try:
                with open("Bootcamp python//2. Intermediate level//Day_29//data.json", mode = "r") as data:
                    r_data = json.load(data)
                    r_data.update(new_data)
            except FileNotFoundError:
                with open("Bootcamp python//2. Intermediate level//Day_29//data.json", mode = "w") as data:
                    json.dump(new_data, data, indent = 4)
            else:
                with open("Bootcamp python//2. Intermediate level//Day_29//data.json", mode = "w") as data:
                    json.dump(r_data, data, indent = 4)
            finally:
                messagebox.showinfo(title = "Success", message = "Your entry was saved successfully!")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    try:
        with open("Bootcamp python//2. Intermediate level//Day_29//data.json", mode = "r") as data:
            contents = json.load(data)
        messagebox.showinfo(title = website_entry.get(), message = f"Email/Username: {contents[website_entry.get()]["Email"]}\nPassword: {contents[website_entry.get()]["Password"]}")
    except:
        messagebox.showerror(title = "Oops", message = "No details of this website found.")
    
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = BLACK)
canvas = Canvas(width = 250, height = 250, bg = BLACK, highlightthickness = 0)
logo = "Bootcamp python//2. Intermediate level//Day_29//logo.png"
lock_image = PhotoImage(file = logo)
canvas.create_image(125, 100, image = lock_image)
canvas.grid(column = 1, row = 0)

#Labels
website_label = Label(text = "Website: ", fg = WHITE, bg = BLACK, font = (FONT_NAME, 10, "normal"))
website_label.grid(column = 0, row = 1)

user_label = Label(text = "Email/Username: ", fg = WHITE, bg = BLACK, font = (FONT_NAME, 10, "normal"))
user_label.grid(column = 0, row = 2)

password_label = Label(text = "Password: ", fg = WHITE, bg = BLACK, font = (FONT_NAME, 10, "normal"))
password_label.grid(column = 0, row = 3)

#Entries
website_entry = Entry(width = 41, fg = WHITE, bg = BLACK, insertbackground = WHITE)
website_entry.grid(column = 1, row = 1)
website_entry.focus()

user_entry = Entry(width = 60, fg = WHITE, bg = BLACK, insertbackground = WHITE)
user_entry.grid(column = 1, row = 2, columnspan = 2)
user_entry.insert(0, "Dashingdash@gmail.com")

password_entry = Entry(width = 41, fg = WHITE, bg = BLACK, insertbackground = WHITE)
password_entry.grid(column = 1, row = 3)

#Buttons
add = Button(text = "Add", width = 51, fg = WHITE, bg = BLACK, command = save)
add.grid(column = 1, row = 4, columnspan = 2)

generate_password = Button(text = "Generate Password", width = 15, fg = WHITE, bg = BLACK, command = generate)
generate_password.grid(column = 2, row = 3)

search = Button(text = "Search", width = 15, fg = WHITE, bg = BLACK, command = search_password)
search.grid(column = 2, row = 1)

window.mainloop()
