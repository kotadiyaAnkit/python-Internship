class CatchException:
    def __enter__(self): #This method is called at the beginning 
        return self

    def __exit__(self, exc_type, exc_val, exc_tb): #Logs the exception using the logging module.
        if exc_type:
            print(f"Exception caught: {exc_val}")
            return True  # Don't raise the error again

print("Program started")

#catchException().__enter__() and assigns the result to x.
with CatchException(): # context managers — objects  up when you enter a block of code and clean it up when you leave it.

    print("Inside with block")
    x = 1 / 2  # This will cause ZeroDivisionError

print("Program continues after the with block")
