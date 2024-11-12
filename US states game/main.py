#US States Game

import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.bgcolor("black")
screen.setup(height = 485, width = 725)
image = "Bootcamp python//2. Intermediate level//Day_25//blank_US_states.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("Bootcamp python//2. Intermediate level//Day_25//US_states.csv")
all_states = states["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 states guessed.", prompt = "Enter state: ").title()
    if answer_state == "Exit":
        unguessed_states = [state for state in all_states if state not in guessed_states]
        remaining_states = pandas.DataFrame(unguessed_states)
        remaining_states.to_csv("Bootcamp python//2. Intermediate level//Day_25//remaining states.csv")
        print(f"\nYou missed the following {len(remaining_states)} states: ")
        print(remaining_states)
        break
    if answer_state not in guessed_states:
        if answer_state in all_states:
            guessed_states.append(answer_state)
            x_state = states[states["state"] == answer_state.title()]["x"].item()
            y_state = states[states["state"] == answer_state.title()]["y"].item()
            tim = turtle.Turtle()
            tim.hideturtle()
            tim.penup()
            tim.color("black")
            tim.goto(x_state, y_state)
            tim.write(answer_state)

if len(guessed_states) == 50:
        print("Well done! You win.")





















