user_input = input("Enter attribute name: ")

try:
    if user_input != "name":
        raise AttributeError(f"'{user_input}' is not a valid attribute.")
    else:
        print("Attribute is valid.")
except AttributeError :
    print("Manually raised:")



