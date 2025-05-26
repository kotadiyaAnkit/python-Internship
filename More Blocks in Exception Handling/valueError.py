def valuseError():
    try:
        age = int(input("Enter your age:"))
    except ValueError:
        print("That's not a valid number!")
    else:
        print("Your age is:", age)
        

valuseError()