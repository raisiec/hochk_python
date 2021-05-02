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
      print(country, city)
      the_world[country] = city

root = Tk()
root.withdraw()
the_world = {}

read_from_file()

print(the_world)

while True:
  query_country = simpledialog.askstring('Country', 'Type The Name of a Country:')

  # How to print the user input data to your console?
  print(query_country)

# End of Program
