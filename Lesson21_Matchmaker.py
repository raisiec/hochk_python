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
