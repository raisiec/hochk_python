# Hour of Code - Ask Expert
# Author: Raisie
# Date: May 2, 2021

from tkinter import Tk, simpledialog, messagebox

print('Ask The Expert - Capital City of The World')

# This function handles the file reading from a data file
def read_from_file():
  with open('Capital_City.txt') as file:
    for line in file:
      line = line.rstrip('\n')
      country, city = line.split('/')
      the_world[country] = city

root = Tk()
root.withdraw()
the_world = {}

read_from_file()

while True:
  query_country = simpledialog.askstring('Country', 'Type The Name of a Country:')

  if query_country in the_world:
    result = the_world[query_country]
    print(result)

    messagebox.showinfo('Answer', 'The Capital City of ' + query_country + ' is ' + result + ' !')
  else:
    print('This Country is Not in The Data Base')
    new_city = simpledialog.askstring('Teach Me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + '?')
    print(new_city)

# End of Program
