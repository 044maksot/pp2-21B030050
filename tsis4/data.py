# Python date
# 1. Write a Python program to subtract five days from current date.
import datetime
a = datetime.date.today()
a = a.replace(day = a.day - 5)
print(a)
print()

# 2. Write a Python program to print yesterday, today, tomorrow.
import datetime
today = datetime.date.today()
yesterday = today.replace(day = today.day - 1)
tomorrow = today.replace(day = today.day + 1)
print("yesterday: ", yesterday)
print("today: ", today)
print("tomorrow: ", tomorrow)
print()

# 3. Write a Python program to drop microseconds from datetime.
import datetime
print(datetime.datetime.now().replace(microsecond = 0))
print()

# 4. Write a Python program to calculate two date difference in seconds.
import datetime
today = datetime.datetime.today()
date = datetime.datetime(2022, 2, 20)
diff = today - date
print(diff.total_seconds())