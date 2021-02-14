# Hour of Code HK - File Generation Demo
# Author: Raisie & Daddy
# Date: Feb 13, 2021

import string
import random

# printing lowercase
letters = string.ascii_lowercase
print(letters)

for i in range(30):

    # create a new random filename
    filename = ''
    for j in range(30):
        filename = filename + random.choice(letters)
   
    #filename = ''.join(random.choice(letters) for i in range(10))

    # append file extension
    filename = filename + '.txt'
    f = open(filename, "a")
    f.write("I am a dummy file")
    f.close()
