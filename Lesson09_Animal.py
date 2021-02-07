# Hour of Code HK - animal quiz
# Author: Raisie
# Date: Feb 7,2021

def check_guess(guess,answer):
    global score
#    if guess == answer:
    if guess.lower() == answer.lower():
        print('correct answer')
        score = score + 1
    else:
        print('wrong answer')

# This is the banner
print('Hour of Code HK - Python Workshop')
print('Guess the animal')
score = 0

# Question 1
guess = input('Which bear live in the north pole? ')
check_guess(guess,'polar bear')

# Question 2
guess = input('What is the fastest land animal? ')
check_guess(guess, 'cheetah')

# Question 3
guess = input('Which animal is the largest one on Earth? ')
check_guess(guess, 'blue whale')

print('Your total score is ', score)
