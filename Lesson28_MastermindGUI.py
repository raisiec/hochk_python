# HoCHK: Mastermind Little Game
# Author: Raise C
# Date: 27/2/2021

import pygame
import random
import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# 12 attempts
# color: Red, Green, Blue, White, Yellow (R, G, B, W, Y)

lives = 8
colors = ['R', 'G', 'B', 'W', 'Y']
heart_symbol = u'\u2764'
y_position_base = 300
length = 5

# Prepare a secret color
color_list = ''
for i in range(length):
    color_list = random.choice(colors) + color_list

# Check Hint Function
def check_hint(guess, color_list):
    for i in range(len(color_list)):
        if (color_list[i].lower() == guess.lower()):
            return True
    return False

# Draw Circle Function
def create_circle(x, y, r, canvasName, fill_color): #center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill= fill_color)

# Get input from user  
def check_guess():    
    guess = ''

    if (combo1.get() == 'Red'):
        guess = guess + 'r'
    elif (combo1.get() == 'Green'):
        guess = guess + 'g'
    elif (combo1.get() == 'Blue'):
        guess = guess + 'u'
    elif (combo1.get() == 'White'):
        guess = guess + 'w'
    elif (combo1.get() == 'Yellow'):
        guess = guess + 'y'
    elif (combo1.get() == 'Black'):
        guess = guess + 'b'
    
    if (combo2.get() == 'Red'):
        guess = guess + 'r'
    elif (combo2.get() == 'Green'):
        guess = guess + 'g'
    elif (combo2.get() == 'Blue'):
        guess = guess + 'u'
    elif (combo2.get() == 'White'):
        guess = guess + 'w'
    elif (combo2.get() == 'Yellow'):
        guess = guess + 'y'
    elif (combo2.get() == 'Black'):
        guess = guess + 'b'

    if (combo3.get() == 'Red'):
        guess = guess + 'r'
    elif (combo3.get() == 'Green'):
        guess = guess + 'g'
    elif (combo3.get() == 'Blue'):
        guess = guess + 'u'
    elif (combo3.get() == 'White'):
        guess = guess + 'w'
    elif (combo3.get() == 'Yellow'):
        guess = guess + 'y'
    elif (combo3.get() == 'Black'):
        guess = guess + 'b'
        
    if (combo4.get() == 'Red'):
        guess = guess + 'r'
    elif (combo4.get() == 'Green'):
        guess = guess + 'g'
    elif (combo4.get() == 'Blue'):
        guess = guess + 'u'
    elif (combo4.get() == 'White'):
        guess = guess + 'w'
    elif (combo4.get() == 'Yellow'):
        guess = guess + 'y'
    elif (combo4.get() == 'Black'):
        guess = guess + 'b'
        
    if (combo5.get() == 'Red'):
        guess = guess + 'r'
    elif (combo5.get() == 'Green'):
        guess = guess + 'g'
    elif (combo5.get() == 'Blue'):
        guess = guess + 'u'
    elif (combo5.get() == 'White'):
        guess = guess + 'w'
    elif (combo5.get() == 'Yellow'):
        guess = guess + 'y'
    elif (combo5.get() == 'Black'):
        guess = guess + 'b'
        
    global y_position_base

    # show 4 colors
    for i in range(length):
        if (guess[i].lower() == 'r'):
            fill_color = 'Red'
        elif (guess[i].lower() == 'g'):
            fill_color = 'Green'
        elif (guess[i].lower() == 'u'):
            fill_color = 'blue'
        elif (guess[i].lower() == 'w'):
            fill_color = 'white'
        elif (guess[i].lower() == 'y'):
            fill_color = 'yellow'
        elif (guess[i].lower() == 'b'):
            fill_color = 'black'
        else:
            fill_color = 'orange'
        create_circle(50 + i*100, y_position_base, 20, c, fill_color)

    # show 4 hints
    # * = Black, o = White
    hint_list = ''
    for i in range(length):
        if(guess[i].lower() == color_list[i].lower()):
            hint = '*'
        elif check_hint(guess[i], color_list):
            hint = 'o'
        else:
            hint = '?'   
        hint_list = hint_list + hint   
    
    for i in range(length):
        if(hint_list[i] == '*'):
            fill_color = 'black'
        elif(hint_list[i] == 'o'):
            fill_color = 'grey'
        else:
            fill_color = 'white'
        create_circle(550 + i*50, y_position_base,10, c, fill_color)
        
    y_position_base = y_position_base + 50

    if (guess.lower() == color_list.lower()):
        c.create_text(50,600,anchor='w',fill='green',font='Arial 28 bold',\
              text='You are Correct! Congratulations!')
        c.delete('sorry_message')
    else:
        c.create_text(150,600,anchor='w',fill='red',font='Arial 28 bold',\
              text='Sorry! Please try again!', tag = "sorry_message")

# Main Loop
root = tk.Tk()
c = Canvas(root, width=800, height=700, bg='white')
c.pack()

c.create_text(100,50,anchor='w',fill='orange',font='Arial 28 bold underline',text='HoCHK Mastermind Game')

label1 = tk.Label(root, text='Make your guess (5 colors)')
label1.config(font=('helvetica', 18))
c.create_window(200, 150, window=label1)

# Create combox for selection
combo1 = Combobox(root, values=['Red','Green','Blue','White','Yellow','Black'], width=5)
c.create_window(100, 200, window=combo1)

combo2 = Combobox(root, values=['Red','Green','Blue','White','Yellow','Black'], width=5)
c.create_window(200, 200, window=combo2)

combo3 = Combobox(root, values=['Red','Green','Blue','White','Yellow','Black'], width=5)
c.create_window(300, 200, window=combo3)

combo4 = Combobox(root, values=['Red','Green','Blue','White','Yellow','Black'], width=5)
c.create_window(400, 200, window=combo4)

combo5 = Combobox(root, values=['Red','Green','Blue','White','Yellow','Black'], width=5)
c.create_window(500, 200, window=combo5)

button1 = tk.Button(text='I am Ready!', command=check_guess, bg='brown', fg='black', font=('helvetica', 14))
c.create_window(600, 150, window=button1)

root.mainloop()
# End of Program
