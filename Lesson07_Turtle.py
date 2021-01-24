# Hour of Code HK - Python Workshop #4
# Author: Raisie C
# Date: Jan 17, 2021
# Date: Jan 24, 2021 (v2)

# Use Random , Turtle
import random
import turtle as t

# Function -> Get Line Length()
# Parameter list -> Empty
# Get user input to define the line length

def get_line_length(): # alternative getLineLength()

    # get input from user via "Standard Input (stdin)"
    choice = input('Enter line length "long, medium, short": ')

    # Check pre-defined string
    if choice == 'long':
        line = 250
    elif choice == 'medium':
        line = 200
    else:
        line = 100

    # return a value to the caller
    return line

# Function -> Get Line Width()
# Parameter List -> Empty
# User input: (superthick, thick, thin) -> 40, 25, 10
def get_line_width():
    choice = input('Enter line width "superthick, thick, thin": ')
    
    print(choice)
    if choice == 'superthick':
        line = 40
    elif choice == 'thick':
        line = 25
    else:
        line = 10
    return line

# Function *TODO* -> Inside Window()
# Give a bounding box for the movement of the turtle



# Function *TODO* -> Move Turtle()
# Control the randomized movement of the Turtle
def move_turtle(line_length):

    # a collection of color
    pen_color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    t.pencolor(random.choice(pen_color))
    t.fillcolor(random.choice(pen_color))

    # Stamp the turle on the screen
    t.shapesize(3,3,1)
    t.stamp()

    # control movement
    t.right(45)
    t.forward(line_length)

# main program
line_length = get_line_length()
line_width = get_line_width()

t.shape('turtle')
t.pensize(line_width)

# An Infinite Loop for the turtle movement
while True:
    move_turtle(line_length)
