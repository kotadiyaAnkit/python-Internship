#datetime.timedelta: Represents a duration of time, useful for adding or subtracting time from datetime objects.
import datetime
now = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
tomorrow = now + one_day
print(tomorrow)