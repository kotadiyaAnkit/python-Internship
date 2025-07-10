def Account(CheckingAccount):
    def SavingsAccount():
        print("\n Calling the function")
        CheckingAccount()  # Call the function passed as an argument
        print("\n After calling the function")
    return SavingsAccount

@Account

def user():
    print("Enter an ID")

# Call the decorated function
user()


