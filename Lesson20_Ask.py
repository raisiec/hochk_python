# Hour of Code - Ask Expert
# Author: Raisie
# Date: May 2, 2021 v1
#       May 9, 2021 v2
#       May 16, 2021 v3

from tkinter import Tk, simpledialog, messagebox

print('Ask The Expert - Capital City of The World')

# This function handles the file reading from a data file
def read_from_file():
  with open('Capital_City.txt') as file:
    for line in file:
      line = line.rstrip('\n')
      country, city = line.split('/')
      the_world[country] = city

# This function will collect user input, and store data onto a file
def write_to_file(country_name, city_name):
  with open('Capital_City.txt','a') as file:
    file.write('\n' + country_name + '/' + city_name)

root = Tk()
root.withdraw()
the_world = {}
read_from_file()

# This is the main loop of this program
while True:
  query_country = simpledialog.askstring('Country', 'Type The Name of a Country:')

  # Check if the country is listed on the database
  if query_country in the_world:
    result = the_world[query_country]
    messagebox.showinfo('Answer', 'The Capital City of ' + query_country + ' is ' + result + ' !')
  else:
    print('This Country is Not in The Data Base')
    new_city = simpledialog.askstring('Teach Me', 'I don\'t know! ' + 'What is the capital city of ' + query_country + '?')

    write_to_file(query_country, new_city)

# End of Program
