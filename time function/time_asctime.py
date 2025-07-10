#time.asctime(): Converts a time tuple to a human-readable string.

import time
time_tuple = time.localtime()
time_string = time.asctime(time_tuple)
print(time_string)