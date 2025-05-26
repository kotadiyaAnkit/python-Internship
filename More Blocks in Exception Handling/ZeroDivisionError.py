def divide_numbers():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))
        result = a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print("Division successful:", result)
    finally:
        print("This is the final block.")


divide_numbers(9,9)
