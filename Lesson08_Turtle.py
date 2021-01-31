# Hour of Code HK - Python Workshop #4
# Author: Raisie C
# Date: Jan 17, 2021
# Date: Jan 24, 2021 (v2)
# Date: Jan 31, 2021 (v3)

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
def inside_window():

    border = 200
    
    left_limit      = (-t.window_width () / 2) + border
    right_limit     = ( t.window_width () / 2) - border
    top_limit       = ( t.window_height() / 2) - border
    bottom_limit    = (-t.window_height() / 2) + border

    print(left_limit, right_limit, top_limit, bottom_limit)

    (x,y) = t.pos()

    inside = (left_limit < x < right_limit) and (bottom_limit < y < top_limit)
    
    return inside
    
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
  #  t.right(45)
  #  t.forward(line_length)

    if inside_window():
        angle = random.randint(0, 180)
        t.right(angle)
        t.forward(line_length)
    else:
        t.backward(line_length)

# main program
line_length = get_line_length()
line_width = get_line_width()

t.shape('turtle')
t.pensize(line_width)

print(t.window_width())
print(t.window_height())

# An Infinite Loop for the turtle movement
while True:
    move_turtle(line_length)
