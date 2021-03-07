# Hour of Code HK - Python Module #6
# Author: Raisie C
# Date: Feb 22 V1, Feb 28, V2, Mar 7, V3

from tkinter import Tk, Canvas
from datetime import date, datetime

# Read data from the event file
def get_events():
  list_events = []
  #print(list_events)
  with open('events.txt') as file:
    for line in file:
      line = line.rstrip('\n')
      current_event = line.split(',')
      event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
      current_event[1] = event_date
      list_events.append(current_event)
  return list_events

# To compare the difference between two given dates
def between_days(date1, date2):
  # date 1 - date 2 = how many days in between?
  #print(type(date1), type(date2))
  print('A', date1 - date2)

  time_between = str(date1 - date2)
  print('B', time_between)

  number_of_days = time_between.split(' ')
  print('[0]:', number_of_days[0], '[1]:', number_of_days[1], '[2]:', number_of_days[2])

# Create a Canvas for display      
root = Tk()
c = Canvas(root, width=800, height=800, bg='red')
c.pack()

# Add text for the Canvas
c.create_text(100,50,text='My countdown calendar')

# get event list from a file
events = get_events()
# create a datetime object for comparison
today = date.today()

# looping the items in events list
for event in events:
  event_name = event[0]
  event_date = event[1]
  #print(event_name, event_date)
  days_until = between_days(event_date, today)
