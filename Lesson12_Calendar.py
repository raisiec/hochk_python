from tkinter import Tk, Canvas
from datetime import date, datetime

# Read data from the event file
def get_events():
  list_events = []
  #print(list_events)
  with open('events.txt') as file:
    for line in file:
      line = line.rstrip('\n')
      #print(line)
      current_event = line.split(',')
      #print(current_event)

      print(current_event[0], type(current_event[0]))
      print(current_event[1], type(current_event[1]))

      event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
      print(event_date, type(event_date))
      current_event[1] = event_date
      list_events.append(current_event)

# Create a Canvas for display      
root = Tk()
c = Canvas(root, width=800, height=800, bg='red')
c.pack()

# Add text for the Canvas
c.create_text(100,50,text='My countdown calendar')

# get event list from a file
events = get_events()
