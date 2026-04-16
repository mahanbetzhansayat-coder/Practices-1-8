from datetime import datetime, timedelta

# Task 1: Subtract five days from current date
current_date = datetime.now()
print("Current Date:", current_date.date())
print("5 Days Ago:", (current_date - timedelta(days=5)).date())

# Task 2: Print yesterday, today, tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("\nYesterday:", yesterday.date())
print("Today:    ", today.date())
print("Tomorrow: ", tomorrow.date())

# Task 3: Drop microseconds from datetime
dt = datetime.now()
print("\nOriginal time:", dt)
print("Without microseconds:", dt.replace(microsecond=0))

# Task 4: Calculate date difference in seconds
date1 = datetime(2024, 1, 1, 12, 0, 0)
date2 = datetime(2024, 1, 1, 12, 0, 10)
diff = date2 - date1
print("\nDifference in seconds:", diff.total_seconds())