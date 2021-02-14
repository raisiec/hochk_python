# Hour of Code HK - riddle quiz
# Author: Raisie
# Date: Feb 14,2021

def check_guess(guess,answer):
    global score
    
    if guess.lower() == answer.lower():
        print('correct answer')
        score = score + 1
    else:
        print('wrong answer')

# This is the banner
print('Hour of Code HK - Python Workshop')
print('Guess the riddle')

score = 0

# Read two files
q = open('riddle_question.txt')
qcontent = q.read()

a = open('riddle_answer.txt')
acontent = a.read()

# split into arrays
question = qcontent.splitlines()
answer = acontent.splitlines()

# list out the questions
for i in range(len(question)):
    guess = input(question[i])
    check_guess(guess, answer[i])

# count the total score
print('Your total score is ', score)
