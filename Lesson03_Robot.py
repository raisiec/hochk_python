# Hour of Code Hong Kong
# 快樂寫程式．輕鬆學Python #1 out of 12 - 機械人產生器
# Author: Raisie & Daddy
# Date: 6 Dec, 2020 v1.0
# Date: 13 Dec, 2020 v2.0
# Date: 27 Dec, 2020 v3.0 

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

# Create a function called "Triangle"
# Parameter:    Input -> Length of the triangle
#               Input -> Color of the triangle
def triangle(length,color):
    t.pendown()
    t.color(color)
    t.begin_fill()
    for c in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()
    t.penup()

# Create the grid for finding the coordinate
for i in range(-400,400,40):
    for j in range (-400,400,40):
        t.goto(i,j)
        rect(1,1,'yellow')

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

#arm
t.goto(-150,70)
rect(60,15,'purple')
t.goto(-150,110)
rect(15,40,'purple')

#hand
t.color('green')
t.goto(-143,105)
t.begin_fill()
t.circle(10)
t.end_fill()

#arm
t.goto(10,70)
rect(60,15,'purple')
t.goto(55,110)
rect(15,40,'purple')

#hand
t.color('green')
t.goto(63,105)
t.begin_fill()
t.circle(10)
t.end_fill()

#neck
t.goto(-50, 120)
rect(15,20,'yellow')

#head
t.goto(-85,170)
rect(80,50,'red')

#hat
t.goto(-85,170)
triangle(80,'green')

#eyes
t.goto(-60,160)
rect(30,10,'white')
t.goto(-55,157)
rect(5,5,'black')
t.goto(-40,157)
rect(5,5,'black')

#mouth
t.goto(-65,135)
rect(40,5,'blue')

# Hide the turtle on the screen
t.hideturtle()

#End of the program












