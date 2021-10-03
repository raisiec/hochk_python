# Coder: Raisie & daddy
# Date: 12/9/2021 & 3/10/2021
# Project: Snake Game

import turtle as t
import random

# Create the Snake object
t.bgcolor('white')
c = t.Turtle()
c.shape('square')
c.color('red')
c.speed(2)
c.penup()

#while True:
#  cater.forward(1)

# Create the Leaf object
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.speed(0)

leaf.setx(0)
leaf.sety(0)
leaf.showturtle()

# Create a Text object
text = t.Turtle()
text.write('Press SPACE to start', align='center', font=('Arial', 16, 'bold'))
text.hideturtle()

# Create a score object

score_turtle = t.Turtle()
score_turtle.hideturtle()

# This function will determine whether the snake is off the bounding window?
def outside_window():
  pass

# This function will be executed when the game is over
def game_over():
  pass

# This function will update the score turtle on the screen
def display_score():
  pass

# This function will randomly place a place on the screen
def place_leaf():

  leaf.penup()
  leaf.ht()
  leaf.setx(random.randint(-200,200))
  leaf.sety(random.randint(-200,200))
  leaf.st()

# The following 4 functions will control the movement of the snake
def move_up():
  c.setheading(90)

def move_down():
  c.setheading(270)

def move_left():
  c.setheading(180)

def move_right():
  c.setheading(0)

# The following function will be executed when the game is ready to start
def start_game():

  text.clear()
  c_speed = 0.5
  c_length = 2
  c.shapesize(1,c_length,1)

  # Snake eating the leaf -> longer

  place_leaf()

  while True:
    c.forward(c_speed)
    if c.distance(leaf) < 20:
      place_leaf()
      c_length = c_length + 1
      c.shapesize(1, c_length, 1)
      c_speed = c_speed + 0.5


# Respond to the keyboard input from the player
t.onkey(start_game,'space')
t.onkey(move_up, 'Up')
t.onkey(move_right, 'Right')
t.onkey(move_down, 'Down')
t.onkey(move_left, 'Left')
t.listen()
t.mainloop()
