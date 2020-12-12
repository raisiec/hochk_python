# Hour of Code Hong Kong
# 快樂寫程式．輕鬆學Python #1 out of 12 - 機械人產生器
# Author: Raisie & Daddy
# Date: 7 Dec, 2020

# Rename turtle as t
import turtle as t

# Configuration
t.penup()
t.shape('turtle')
t.bgcolor('dodger blue')
t.speed('fast')

# Create a function called "Rectangle -> Rect, short form"
# Parameter:    Input -> Horizontal width of the rectange
#               Input -> Vertical width of the rectange
#               Input -> Color of the rectange
def rect(horizontal,vertical,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for counter in range(2):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)        
    t.end_fill()
    t.penup()

# Draw two different rectangles at a given location
t.goto(0,0)
rect(100,100,'yellow')

t.goto(0,200)
rect(100,50,'red')

# Hide the turtle on the screen
t.hideturtle()
