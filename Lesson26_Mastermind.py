# HoCHK: Mastermind little Game
# Author: Raisie C, Daddy
# Date: 5/3/2022

import random

# Variable used
lives = 10
heart_symbol = u'\u2764'
colors = ['R', 'G', 'B', 'W', 'Y']

# Ask player for the difficulty of this game
length = int(input('\nWhat is the length of the secret color (2 / 3 / 4 / 5)? '))

# Prepare the secret color list for guessing
color_list = ''
for i in range(length):
  color_list = color_list + random.choice(colors) 
  #print(color_list)

# Main loop
while (lives > 0):
  print('lives left:' + heart_symbol * lives)
  guess = input('\nWhat is the secret color (R, G, B, W, Y)? ')

  if (color_list!= guess):
    lives = lives - 1
    print('You lost! Please try again!\n')
  else:
    print('You got the color correct!\n')
    break

# END
