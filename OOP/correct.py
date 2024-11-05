import itertools
from datetime import datetime, timedelta

# Constants
EMPLOYEE = list(range(1, 21))
START_TIME = datetime.strptime("09:00", "%H:%M")
END_TIME = datetime.strptime("17:00", "%H:%M")
WORK_DAYS = 5  # Monday to Friday
MEETING_DURATION = timedelta(hours=1)
ROOMS = 2

# Generate all unique pairs of employees for meetings
all_pairs = list(itertools.combinations(EMPLOYEE, 2))
total_meetings_needed = len(all_pairs)

# Schedule dictionary
schedule = {day: [] for day in range(1, WORK_DAYS + 1)}

def find_available_time(day_schedule):
    """Finds the next available time slot with room availability."""
    if not day_schedule:
        return START_TIME

    time = START_TIME
    while time < END_TIME:
        # Count meetings happening at the current time slot
        active_meetings = sum(1 for m in day_schedule if m[1] == time)
        if active_meetings < ROOMS:
            return time
        time += MEETING_DURATION
    return None

# Schedule meetings for each day
day = 1
for pair in all_pairs:
    available_time = find_available_time(schedule[day])

    if available_time:
        # Schedule the meeting in the available slot
        schedule[day].append((pair, available_time))
    else:
        # Move to the next day
        day += 1
        if day > WORK_DAYS:
            day = 1
        schedule[day].append((pair, START_TIME))

# Print the schedule
for day, meetings in schedule.items():
    print(f"Day {day} schedule:")
    for meeting in meetings:
        pair, time = meeting
        print(f"  Employees {pair[0]} and {pair[1]} at {time.strftime('%H:%M')}")
