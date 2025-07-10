#time.strftime(format, time_tuple): Formats a time tuple into a string based on the provided format codes.

import time
time_tuple = time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
print(formatted_time)

#time.sleep(seconds): Pauses the execution of the program for the specified number of seconds.