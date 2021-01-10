# Hour of Code HK - Python Lesson #3
# Author: Raisie C
# Date: Jan 10, 2021

import turtle as t
from random import randint, random

# Function -> Draw_Star() with 5 input parameters
def draw_star(size, points, x, y, color):
    # parameter for the star
    angle = 180 - (180 / points)

    # define the color of the star
    t.color(color)

    # go to a specific location
    t.penup()
    t.goto(x,y)
    t.pendown()
    
    # start filling the star
    t.begin_fill()

    # repeat 5 times
    for i in range(points):
        # draw line
        t.forward(size)
        # turn angle
        t.right(angle)

    # end filling the star
    t.end_fill()

# Function -> Draw_Planet() with 4 input parameters
def draw_planet(size, col, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

# Function -> Draw_Moon() with two overlapping Circles
def draw_moon():
    t.up()
    t.goto(250,200)
    t.color('orange')
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.up()
    t.goto(300,200)
    t.color('dark blue')
    t.begin_fill()
    t.circle(100)
    t.end_fill()

# Select the Background Color of the Screen
t.Screen().bgcolor('dark blue')
t.speed(0)

# Draw one Moon here
draw_moon()

# Draw the Stars over the Sky
while True:  
    # define parameters for the stars
    # size
    ranSize = randint(10,50)
    # points
    ranPts = randint(2,5) * 2 + 1
    # x, y
    ranX = randint(-500, 500)
    ranY = randint(-400, 400)
    # color
    ranColor = (random(), random(), random())
    
    # Draw Star or Draw Planet (50% Star and 50% Planet)
    if (randint(1,2) == 1):
        draw_star(ranSize, ranPts, ranX, ranY, ranColor)
    else:
        draw_planet(ranSize/2, ranColor, ranX, ranY)

# End of the Program
