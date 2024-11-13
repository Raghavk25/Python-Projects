FONT = ("Courier", 24, "bold")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
    
    def display_level(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.color("white")
        self.write(f"Level: {self.level}", align = "left", font = FONT)
    
    def level_up(self):
        self.level += 1
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = "center", font = FONT)


        