#German to English flash cards

# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from tkinter import *
import random
import pandas
import time
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("./German_frequency_list.csv")
word_dict = {row.German: row.English for (index, row) in data.iterrows()}
r_word = {}

#---------------------------------- Card flipping system -----------------------------------#
def generate_random_word():
    canvas.itemconfig(page, image = card_front)
    global r_word
    global flip_timer
    window.after_cancel(flip_timer)
    r_index = random.randint(0, 2022)
    r_word = data["German"].iloc[r_index]
    canvas.itemconfig(title, text = "German", fill = "black")
    canvas.itemconfig(word, text = r_word, fill = "black")
    flip_timer = window.after(3000, func = flip_card)

def flip_card():
    canvas.itemconfig(page, image = card_back)
    canvas.itemconfig(title, text = "English", fill = "white")
    canvas.itemconfig(word, text = word_dict[r_word], fill = "white")
#---------------------------------- UI setup -----------------------------------#
window = Tk()
window.title("German to English")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

flip_timer = window.after(3000, func = flip_card)

canvas = Canvas(width = 800, height = 526)
card_back = PhotoImage(file = "./card_back.png")
card_front = PhotoImage(file = "./card_front.png")
page = canvas.create_image(400, 263, image = card_front)
title = canvas.create_text(400, 150, text = "", font = ("Arial", 40))
word = canvas.create_text(400, 263, text = "", font = ("Arial", 40, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.grid(column = 0, row = 0, columnspan = 2)

right_image = PhotoImage(file = "./right.png")
right_button = Button(image = right_image, highlightthickness = 0, command = generate_random_word)
right_button.grid(column = 1, row = 1)

wrong_image = PhotoImage(file = "./wrong.png")
wrong_button = Button(image = wrong_image, highlightthickness = 0, command = generate_random_word)
wrong_button.grid(column = 0, row = 1)

generate_random_word()

window.mainloop()
