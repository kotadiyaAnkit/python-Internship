# main.py
from login import log_function_call  # Import from decorators.py

@log_function_call
def say_hello():
    print("Hello, world!")

say_hello()
