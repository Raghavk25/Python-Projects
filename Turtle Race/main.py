#Turtle Race

import turtle
import random
import time

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
screen = turtle.Screen()
screen.setup(width = 800, height = 492)
user_bet = screen.textinput(title = "Make a bet", prompt = "Which turtle will win the race? Enter a color: ").lower()
print(f"Your bet: {user_bet.title()}")
all_turtles = []

if user_bet not in colors:
    print("Sorry, that's not in the color range. Pick a rainbow color.")
else:
    for i in range(7):
        new_turtle = turtle.Turtle(shape = "turtle")
        new_turtle.color(colors[i])
        new_turtle.up()
        new_turtle.goto(x = -387, y = -187 + 65 * i)
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    for j in range(3):
        turtle.hideturtle()
        turtle.write(f"{3 - j}", font=("Arial", 60))
        time.sleep(1)
        turtle.clear()
    
    turtle.write("GO!", font=("Arial", 60))
    time.sleep(1)
    turtle.clear()
    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() >= 360:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print("\nCongratulations, you won!")
                else:
                    print(f"\nPsst, you lost. {winning_color.title()} won the race.")
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

    screen.exitonclick()
