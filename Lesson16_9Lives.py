# Hour of Code HK - Nine Lives
# Author: Raisie C
# Date: April 4, 2021

# Import package
import random

# Define program parameters
lives = 9
heart_symbol = u'\u2764'

words = ['eel', 'cat', 'sos', 'shy', 'fun', 'fan', 'kid', 'zoo', 'egg', 'fat']
secret_word = random.choice(words)

# Main Loop
while lives > 0:
  print('Lives left: ' + heart_symbol * lives)

  # Get user input
  guess = input('Guess A Word: ')
  print('user input: ' + guess)
  
  # Check if the answer is correct
  if guess == secret_word:
    print('You are correct! Bingo!')
    break
  else:
    print('Sorry, you are wrong! You lose a life!')
    lives = lives - 1

# end of program
