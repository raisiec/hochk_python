# Hour of Code Hong Kong
# 快樂寫程式．輕鬆學Python #2 out of 12 - 旋轉萬花筒
# Author: Raisie & Daddy
# Date: Jan 3, 2021 v1.0

import turtle as t

# Use iterators for efficient looping
from itertools import cycle

# Create a list of colors
colors = cycle(['red','orange','yellow','green','blue'])

# Create a function called "Draw Circle"
# Parameter:    Input -> Size of the Circle
#               Input -> Rotation of the Circle
#               Input -> Shift movement of the Turtle
def draw_circle(size, angle, shift):
    t.pencolor(next(colors))  
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    # Call the Draw Circle Function recursively
    draw_circle(size + 5, angle + 1, shift + 1)
    
t.bgcolor('pink')
t.pensize(4)
t.speed(5)

draw_circle(10, 0, 1)

#End of the program
