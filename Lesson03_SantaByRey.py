# Author: Rey Chau, HoCHK Coder
# Date: 12/20/2020

import turtle as t

t.penup()
t.shape('turtle')
t.bgcolor('whitesmoke')
t.speed(2)
t.showturtle()

#eyes    
t.color('dimgray')
t.begin_fill()
t.goto(0,0)
t.goto(-50,50)
t.goto(-100,0)
t.end_fill()

t.color('dimgray')
t.begin_fill()
t.goto(5,0)
t.goto(55,50)
t.goto(105,0)
t.end_fill()

#mouth       
t.color('gainsboro')
t.goto(100,-20)
t.begin_fill()
t.goto(100,-20)
t.goto(2.5,-110)
t.goto(-100,-20)
t.end_fill()

#hat white part   
t.color('orangered')
t.goto(-100,60)
t.begin_fill()
t.goto(-100,60)
t.goto(2.5,150)
t.goto(100,60)
t.end_fill()

#hat red 1
t.color('firebrick')
t.goto(70,85)
t.begin_fill()
t.goto(2.5,150)
t.goto(70,215)
t.goto(70,85)
t.end_fill()

#hat red 2
t.color('tomato')
t.goto(70,150)
t.begin_fill()
t.goto(70,150)
t.goto(140,85)
t.goto(140,150)
t.goto(70,215)
t.end_fill()

#hat yellow part
t.color('gold')
t.goto(140,85)
t.begin_fill()
t.pendown()
t.right(20)
t.forward(50)
for s in range(3):
    t.right(90)
    t.forward(50)
t.end_fill()

t.hideturtle()
