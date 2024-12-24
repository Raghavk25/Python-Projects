#Damien Hirst Spot Painting Painter

import random
import turtle

tim = turtle.Turtle()
turtle.colormode(255)
turtle.bgcolor("black")


# import colorgram

# rgb_colors = []
# colors = colorgram.extract('./Damien_Hirst_Spot.jpg', 120)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b)) 
# print(rgb_colors)   #This was used to extract colors from the image.

color_list = [(249, 248, 248), (238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), 
              (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), 
              (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), 
              (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), 
              (122, 169, 190), (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]
x = -230
y = -230
tim.up()
tim.hideturtle()
tim.goto((x, y))
tim.speed(0)
for i in range(10):
    for j in range(10):
        tim.dot(20, random.choice(color_list))
        tim.up()
        tim.fd(50)
    tim.setpos((x, y + (50 * (i + 1))))

screen = turtle.Screen()
screen.exitonclick()


