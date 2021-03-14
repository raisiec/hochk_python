# Hour of Code HK - Python Lesson 7
# Author: Raisie
# Date: Pi Day 2021

# package used
import random
import string

# Prepare keywords
adjectives = ['sleepy','slow','smelly','wet']

nouns = ['apple','dinosaur','ball','basketball','pi-day']

emojis = ['😃', '🧘🏻‍♂️', '🌍', '🍞', '🚗', '📞', '🎉']

# forever loop
while True:
  adj = random.choice(adjectives)
  noun = random.choice(nouns)
  emoji = random.choice(emojis)
  number = random.randrange(0,100)
  special_char = random.choice(string.punctuation)

  password = adj + noun + str(number) + special_char + emoji
  print('Your new password is: %s' % password)

  # Check user feedback
  response = input('Would you like another password? Type Y or N: ')
  if response == 'n':
    break

# End of Program
