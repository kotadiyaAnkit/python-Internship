#datetime.strftime(format): Formats a datetime object into a string based on format codes.


import datetime
now = datetime.datetime.now()
formatted_date = now.strftime("%Y-%m-%d")
print(formatted_date)