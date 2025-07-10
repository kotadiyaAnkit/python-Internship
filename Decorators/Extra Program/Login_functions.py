def log_function_call(func):
    def wrapper(a, **b):
        print(f"Function name: {func.__name__}")  # Shows the name
        print(f"Arguments: {a}, {b}")     # Shows args and kwargs
        return func(a, **b)              # Calls the original function
    return wrapper

@log_function_call
def greet(name):
    print(f"Hello, {name}!")

greet("milan")