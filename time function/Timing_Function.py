import time

# Define the timing decorator
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()              # Start timer
        result = func(*args, **kwargs)   # Run the function
        end = time.time()                # End timer
        print(f"Function '{func.__name__}' took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)  # Simulates a delay of 2 seconds
    print("Finished slow task!")

slow_function()
