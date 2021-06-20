# Author: Raisie & Daddy
# Date: June 13, 2021
# Project: Matchmaker

import random
import time
from tkinter import Tk, Button, DISABLED

#dict = {'Name': 'Raisie', 'Age': '7', 'Parent': 'Ray'}
#print(dict['Name'], dict['Age'], dict['Parent'])

# Create the Tk Window
root = Tk()
root.title('Matchmaker 2021')
root.resizable(width = False, height = False)

# Variable initialization
buttons = {}
first = True
previousX = 0
previousY = 0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708',
           u'\u2709', u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B',
           u'\u270C', u'\u270C', u'\u270F', u'\u270F', u'\u2712', u'\u2712',
           u'\u2714', u'\u2714', u'\u2716', u'\u2716', u'\u2728', u'\u2728']

print(symbols)

# Randomize the predefined symbols
random.shuffle(symbols)
print(symbols)

def show_symbol(x,y):
  global first
  global previousX, previousY

  print(first)
  print(previousX)
  print(previousY)

  buttons[x, y]['text'] = button_symbols[x, y]
  buttons[x, y].update_idletasks()

  if first:
    previousX = x
    previousY = y
    first = False
  elif previousX != x or previousY != y:
    # if not matched, gives 0.5s for memorizing the icon
    if buttons[previousX, previousY]['text'] != buttons[x,y]['text']:
      time.sleep(0.5)
      buttons[previousX, previousY]['text'] = ''
      buttons[x, y]['text'] = ''
    else:
    # if patterns are matched, disable the two buttons
      buttons[previousX, previousY]['command'] = DISABLED
      buttons[x,y]['command'] = DISABLED
    first = True

# Create a 6 x 4 array buttons
for x in range(6):
  for y in range(4):
    button = Button(command = lambda x=x, y=y: show_symbol(x,y), width=5, height=5)
    button.grid(column=x, row=y)
    buttons[x,y] = button
    button_symbols[x,y] = symbols.pop()

# Tk Mainloop here
root.mainloop()
