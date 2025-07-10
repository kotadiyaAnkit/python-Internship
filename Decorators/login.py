# decorators.py

def log_function_call(func):
    def wrapper():
        print(f"Calling: {func.__name__}")
        func()
        print(f"Finished: {func.__name__}")
    return wrapper

