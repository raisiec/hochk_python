# Hour of Code Hong Kong
# 快樂寫程式．輕鬆學Python #1 out of 12 - 機械人產生器
# Author: Raisie & Daddy
# Date: 13 Dec, 2020 v1.0

# Rename turtle as t
import turtle as t

# Configuration
t.penup()
t.shape('turtle')
t.bgcolor('dodger blue')
t.speed(0)

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

#feet
t.goto(-100,-150)
rect(50,20,'blue')
t.goto(-30,-150)
rect(50,20,'blue')

#legs
t.goto(-25,-50)
rect(15,100,'yellow')
t.goto(-70,-50)
rect(15,100,'yellow')

#body
t.goto(-90,100)
rect(100,150,'tan')

#arms
t.goto(-150,70)
rect(60,15,'purple')
t.goto(-150,110)
rect(15,40,'purple')

t.goto(10,70)
rect(60,15,'purple')
t.goto(55,110)
rect(15,40,'purple')

#neck
t.goto(-50, 120)
rect(15,20,'yellow')

#head


#hat


#eyes


#mouth


# Hide the turtle on the screen
t.hideturtle()
