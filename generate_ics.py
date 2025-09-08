import csv
from ics import Calendar, Event
from datetime import datetime
import pytz

# Function to parse datetime strings and convert from Europe/Zurich to UTC
def parse_datetime(dt_str):
    # Example: '2025-07-17 14:00:00'
    # First, parse the datetime string into a naive datetime object
    local_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")

    # Define the timezone for Europe/Zurich
    zurich_tz = pytz.timezone("Europe/Zurich")

    # Localize the naive datetime object to Europe/Zurich time
    local_time = zurich_tz.localize(local_time)

    # Convert the localized time to UTC
    utc_time = local_time.astimezone(pytz.utc)

    return utc_time

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
