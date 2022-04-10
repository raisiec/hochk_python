# HoCHK: Mastermind little Game
# Author: Raisie C, Daddy
# Date: 5/3/2022 & 10/4/2022

import random
from art import *

# Variable used
lives = 10
heart_symbol = u'\u2764'
colors = ['R', 'G', 'B', 'W', 'Y']
color_list = ''
hint_list = ''

# Ask player for the difficulty of this game
length = int(input('\nWhat is the length of the secret color (2 / 3 / 4 / 5)? '))

# Prepare the secret color list for guessing
for i in range(length):
  color_list = color_list + random.choice(colors) 

def check_hint(guess):
  for i in range(length):
    if (color_list[i].lower() == guess.lower()):
      return True
  return False
  
# Main loop
while (lives > 0):
  print('lives left:' + heart_symbol * lives)
  guess = input('\nWhat is the secret color (R, G, B, W, Y)? ')

  for i in range(length):
    if guess[i].lower() == color_list[i].lower():
      hint = '*'
    elif check_hint(guess[i]):
      hint = 'o'
    else:
      hint = '?'
    hint_list = hint_list + hint

  print('Your Hints are (* = Black, o = White):' + hint_list)

  if (color_list!= guess):
    lives = lives - 1
    tprint('Wrong!')
    print('You lost! Please try again!\n')
  else:
    tprint('Right!')
    print('You got the color correct!\n')
    break

# END
