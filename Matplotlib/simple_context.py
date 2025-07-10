class MyContextManager:
    def __enter__(self):  #This method is called at the beginning 
        print("Entering context")
        return self  # Optional: return something if needed

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# Using the context manager
with MyContextManager():
    print("Inside the with block")
