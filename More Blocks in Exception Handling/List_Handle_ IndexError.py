def acess():
    list = [10, 20, 30, 40, 50]
    try:
        find_number = int(input("Enter an find a number "))
        print(f"Element at index {find_number} is {list[find_number]}")
    except IndexError:
        print("Error: number not found.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# Run the function
acess()
