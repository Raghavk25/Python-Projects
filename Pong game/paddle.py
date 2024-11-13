# MIT License
# Copyright (c) 2024 Raghav Khanna
# See the LICENSE file in the root of the repository for full license details.

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.goto(coordinates)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len = 1, stretch_wid = 5)
    
    def paddle_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def paddle_down(self):
        self.goto(self.xcor(), self.ycor() - 20)

  
