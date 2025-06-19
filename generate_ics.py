import json
from ics import Calendar, Event

# Load JSON data from file
with open("events.json", "r") as f:
    events_data = json.load(f)

# Create a new calendar
calendar = Calendar()

# Process each event and add to the calendar
for event_data in events_data:
    event = Event()
    event.uid = event_data["uid"]
    event.begin = event_data["dtstart"]
    event.end = event_data["dtend"]
    event.name = event_data["summary"]
    event.description = event_data["description"]
    event.location = event_data["location"]
    
    # Add an alarm (if exists)
    if "alarm" in event_data:
        event.alarms = [event_data["alarm"]]

    # Add the event to the calendar
    calendar.events.add(event)

# Save the calendar to an .ics file
with open("events.ics", "w") as f:
    f.writelines(calendar)
