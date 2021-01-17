# Hour of Code HK - Python Workshop #4
# Author: Raisie C
# Date: Jan 17, 2021

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


    
# main program
line_length = get_line_length()
print('The return value is', line_length)

line_width = get_line_width()
print('The return value is', line_width)

t.shape('turtle')
t.fillcolor('green')
t.pensize(line_width)
t.forward(line_length)
