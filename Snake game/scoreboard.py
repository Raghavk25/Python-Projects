# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from turtle import Turtle
FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("Bootcamp python/2. Intermediate level/Day_20-21/data1.txt") as highscore:
            self.high_score = int(highscore.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_score()
  
    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Bootcamp python/2. Intermediate level/Day_20-21/data1.txt", mode = "w") as highscore:
                highscore.write(f"{self.high_score}")
        self.update_score()
        self.goto(0, 0)
        self.write("GAME OVER", align = ALIGNMENT, font = ("Courier", 20, "normal"))

    def update_score(self):
        self.clear()
        self.write(f"Your score: {self.score} | High score: {self.high_score}", align = ALIGNMENT, font = FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_score()
        
