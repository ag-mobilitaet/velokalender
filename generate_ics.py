import csv
from datetime import datetime
from icalendar import Calendar, Event

# Function to parse datetime strings (adjust format as needed)
def parse_datetime(dt_str):
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

# Create a new calendar
calendar = Calendar()
calendar.add('X-WR-CALNAME', 'Velokalender')

# Load data from CSV
with open("events.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        event = Event()

        # Set event attributes
        event.add('uid', row["uid"])
        event.add('dtstart', parse_datetime(row["dtstart"]))
        event.add('dtend', parse_datetime(row["dtend"]))
        event.add('summary', row["summary"])
        event.add('description', row["description"])
        event.add('location', row["location"])

        # Add event to calendar
        calendar.add_component(event)

# Save the calendar to an .ics file
with open("events.ics", "wb") as f:
    f.write(calendar.to_ical())
