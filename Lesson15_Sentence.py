# Title
# Hour of Code HK - Python Lesson 8
# Author: Raisie C
# Date: March 28, 2021

import random
import string
from tkinter import Tk, Canvas

# Banner
print('Hour of Code Hong Kong')
print('Welcome to Sentence Generator\n')

# Noun list
noun_list = ['apple', 'dinosaur', 'ball', 'goat']

# Adjective list
adjective_list = ['sleepy', 'slow', 'smelly', 'wet']

# Adverb list
adverb_list = ['slowly', 'bravely', 'angrily', 'sadly']

# Verb list
verb_list = ['run', 'eat', 'fly', 'walk']

# Create a Canvas for display      
root = Tk()
c = Canvas(root, width=800, height=800, bg='red')
c.pack()

# Add text for the Canvas
c.create_text(100,50,text='My Sentence Generator')
vertical_position = 100

# Generate 20 randomized sentences
for i in range(20):
  noun = random.choice(noun_list)
  adj = random.choice(adjective_list)
  adv = random.choice(adverb_list)
  verb = random.choice(verb_list)
  my_sentence = 'My super sentence is: ' + noun + ' ' + verb + ' ' + adj + ' ' + adv
  print(my_sentence)

  c.create_text(150, vertical_position, text=my_sentence)
  vertical_position = vertical_position + 30

# end of program
