# HoCHK: Mastermind little Game
# Author: Raisie C, Daddy
# Date: 5/3/2022

import random

lives = 10
heart_symbol = u'\u2764'
colors = ['R', 'G', 'B', 'W', 'Y']

length = int(input('\nWhat is the length of the secret color (2 / 3 / 4 / 5)? '))
print(length)

color_list = ''
for i in range(length):
  color_list = color_list + random.choice(colors) 
  print(color_list)

while (lives > 0):
  print('\nWhat is the secret color (R, G, B, W, Y)? ')
  guess = input()
  print(guess)
