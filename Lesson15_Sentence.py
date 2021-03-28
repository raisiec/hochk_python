# Title
# Hour of Code HK - Python Lesson 8
# Author: Raisie C
# Date: March 28, 2021

import random
import string

# Banner
print('Hour of Code Hong Kong')
print('Welcome to Sentence Generator')

# Noun list
noun_list = ['apple', 'dinosaur', 'ball', 'goat']

# Adjective list
adjective_list = ['sleepy', 'slow', 'smelly', 'wet']

# Adverb list
adverb_list = ['slowly', 'bravely', 'angrily', 'sadly']

# Verb list
verb_list = ['run', 'eat', 'fly', 'walk']

# print out the list content
#for i in range(len(noun_list)):
#  print(noun_list[i])

noun = random.choice(noun_list)
adj = random.choice(adjective_list)
adv = random.choice(adverb_list)
verb = random.choice(verb_list)

my_sentence = noun + verb + adj + adv
print(my_sentence)
