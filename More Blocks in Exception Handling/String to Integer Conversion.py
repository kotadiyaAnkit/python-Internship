def convert_to_integer():
    user_input = input("Enter a number: ")
    try:
        number = int(user_input)
        print(f"The integer value is {number}.")
    except ValueError:
        print("Error: Input is not a valid integer.")

# Run the function
convert_to_integer()
