# import time

# def delay_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print("Pausing after execution...")
#         time.sleep(2)
#         return result
#     return wrapper

# @delay_decorator

# def great():
#     print("")
import time

print("Before sleep...")
time.sleep(3)  # Pauses for 3 seconds
print("After sleep...")
