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

      print(current_event[0])
      print(current_event[1])

      event_date = datetime.strptime(current_event[1], '%d/%m/%y').date()
      print(event_date)
      current_event[1] = event_date
      list_events.append(current_event)
  return list_events

# To compare the difference between two given dates
def between_days(date1, date2):
  # To-Do
  pass

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
print('I am now in main loop!')
for event in events:
  event_name = event[0]
  event_date = event[1]
  print(event_name, event_date)
