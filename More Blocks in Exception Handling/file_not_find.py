def open_file():
    filename = input("Enter the filename to open: ")
    try:
        
        with open("D:\\python\\More Blocks in Exception Handling\\xyz.txt", 'r') as file:
            find = file.read()
            print(find)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

open_file()

