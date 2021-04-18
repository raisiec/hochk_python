# Hour of Code HK - Nine Lives
# Author: Raisie C
# Date: April 4, 2021 (v1)
#       April 18, 2021 (v2)

# Import package
import random

# Define program parameters
lives = 9
heart_symbol = u'\u2764'

# Read animal list from a File
a_file = open('animal.txt')
a_content = a_file.read()
words = a_content.splitlines()
secret_word = random.choice(words)

clue = list('*' * len(secret_word))

# Update the clue based on the user input "guess"
def update_clue(guess, secret_word, clue):
  index = 0
  while index < len(secret_word):
    #if guess == secret_word[i], then update clue[i]
    if guess.lower() == secret_word[index].lower():
      clue[index] = guess
    index = index + 1

# Main Loop
while lives > 0:
  print(clue)
  print('\nLives left: ' + heart_symbol * lives)

  # Get user input
  guess = input('Guess A Word: ')
  print('user input: ' + guess)

  # If guess inside secret word, update clue
  if guess in secret_word:
    update_clue(guess, secret_word, clue)
  
  # Check if the answer is correct
  if guess == secret_word:
    print('You are correct! Bingo!')
    break
  else:
    print('Sorry, you are wrong! You lose a life!')
    lives = lives - 1

print('The correct answer is ', secret_word)
# end of program
