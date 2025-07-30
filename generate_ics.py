import csv
from ics import Calendar, Event
from datetime import datetime

# Function to parse datetime strings (adjust format as needed)
def parse_datetime(dt_str):
    # Example: '2025-07-17 14:00:00'
    return datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

# Create a new calendar
calendar = Calendar()

# Load data from CSV
with open("events.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        event = Event()
        event.uid = row["uid"]
        event.begin = parse_datetime(row["dtstart"])
        event.end = parse_datetime(row["dtend"])
        event.name = row["summary"]
        event.description = row["description"]
        event.location = row["location"]

        # Optional alarm (only if present and non-empty)
        if "alarm" in row and row["alarm"].strip():
            event.alarms = [row["alarm"]]  # You may need to convert to Alarm object if needed

        calendar.events.add(event)

# Save the calendar to an .ics file
with open("events.ics", "w", encoding='utf-8') as f:
    f.writelines(calendar)
