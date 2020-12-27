# Hour of Code Hong Kong
# 快樂寫程式．輕鬆學Python #1 out of 12 - 機械人產生器
# Exercise: Tangram Drawing
# Author: Raisie & Daddy
# Date: 27 Dec, 2020 v1.0 

import turtle as t

t.speed(0)
t.pensize(0)
t.hideturtle()
t.bgcolor('dodger blue')

# Create a function called "my_title"
# Parameter:    Input -> Give a name to this title
def my_title(name):
    t.penup()
    t.goto(0, 300)
    t.write(name, align='center', font=('Arial', 20, 'bold'))
    a = input()
    t.goto(0,0)
    t.pendown()
    t.clear()

t.clear()

#Green plate
t.color("green")
t.begin_fill()
t.goto(200,200)
t.goto(-200,200)
t.end_fill()
#Blue plate
t.color("blue")
t.begin_fill()
t.goto(-200,-200)
t.goto(0,0)
t.end_fill()
#Yellow plate
t.color("yellow")
t.begin_fill()
t.goto(100,-100)
t.goto(100,100)
t.end_fill()
#Red plate
t.color("red")
t.begin_fill()
t.goto(200,200)
t.goto(200,0)
t.goto(100,-100)
t.end_fill()
#Purple plate
t.color("purple")
t.begin_fill()
t.goto(0,0)
t.goto(-100,-100)
t.goto(0,-200)
t.end_fill()
# Pink plate
t.color("pink")
t.begin_fill()
t.goto(-100,-100)
t.goto(-200,-200)
t.goto(0,-200)
t.end_fill()
#Orange Plate
t.color("orange")
t.begin_fill()
t.goto(200,-200)
t.goto(200,0)
t.end_fill()
t.penup()
my_title('I am a tangram!')
 
t.clear()

# Create a function called "Draw a 3-sided Polygon"
# Parameter:    Input -> Give a color for the Polygon
#               Input -> Give a 3 points coordinate in this format
#                           Point 1: coord[0][0], coord[0][1]
#                           Point 2: coord[1][0], coord[1][1]
#                           Point 3: coord[2][0], coord[2][1]
def draw_3(color, coord):
    t.color(color)
    t.goto(coord[0][0], coord[0][1])
    t.pendown()
    t.begin_fill()
    t.goto(coord[1][0],coord[1][1])
    t.goto(coord[2][0],coord[2][1])
    t.end_fill()
    t.penup()

# Create a function called "Draw a 4-sided Polygon"
# Parameter:    Input -> Give a color for the Polygon
#               Input -> Give a 4 points coordinate in this format
#                           Point 1: coord[0][0], coord[0][1]
#                           Point 2: coord[1][0], coord[1][1]
#                           Point 3: coord[2][0], coord[2][1]
#                           Point 4: coord[3][0], coord[3][1]
def draw_4(color, coord):
    t.color(color)
    t.goto(coord[0][0], coord[0][1])
    t.pendown()
    t.begin_fill()
    t.goto(coord[1][0],coord[1][1])
    t.goto(coord[2][0],coord[2][1])
    t.goto(coord[3][0],coord[3][1])
    t.end_fill()
    t.penup()

# Create a function called "Draw a Star"
# Parameter:    Input -> Give the x coordinate
#               Input -> Give the y coordinate
#               Input -> Give a color for the star
#               Input -> Give the size of this star
def draw_star(x, y, color, size):
    t.goto(x,y)
    t.color(color)
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.right(145)
    t.end_fill()
    
draw_3("green", [[0,0],[0,200],[-200,0]])
draw_3("blue", [[0,0],[-200,0],[0,-200]])    
draw_4("purple", [[0,-50],[100,-50],[100,50],[0,50]])
draw_3("pink",[[0,50],[100,50],[0,150]])
draw_3("yellow",[[0,-50],[0,-150],[100,-50]])
draw_3("orange",[[100,-50],[300,-50],[200,50]])
draw_4("red",[[100,-50],[200,50],[200,150],[100,50]])

my_title('I am a fish!')

draw_4("yellow",[[-200,0],[-100,100],[0,100],[-100,0]])
draw_3("orange",[[-100,0],[50,150],[225,0]])
draw_3("pink",[[-150,0],[0,0],[-150,-150]])
draw_3("blue",[[-150,-150],[0,0],[150,-150]])
draw_3("purple",[[0,0],[150,0],[78,-78]])
draw_3("red",[[78,-78],[150,0],[150,-150]])

my_title('I am a house!')

t.penup()
draw_3("red",[[-50,150],[50,150],[0,200]])
draw_3("blue",[[-100,50],[100,50],[0,150]])
draw_3("green",[[-150,-100],[150,-100],[0,50]])
draw_4("brown",[[-25,-100],[25,-100],[25,-200],[-25,-200]])

draw_star(-24,220,"yellow",45)
draw_star(-160,-100,"orange",30)
draw_star(140,-100,"orange",30)
draw_star(-110,50,"orange",30)
draw_star(90,50,"orange",30)
draw_star(-60,150,"orange",30)
draw_star(40,150,"orange",30)

t.goto(0,-250)
t.write("Merry Christmas!", align='center', font=('Arial', 20, 'bold'))
t.goto(0,-300)
t.write("By Raisie & Daddy", align='center', font=('Arial', 20, 'bold'))

#End of the Program
