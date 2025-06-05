def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    
    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{marks}\n")
    print("Student added successfully.\n")


def view_students():
    try:
        with open("students.txt", "r") as file:
            print("Student Records:")
            for line in file:
                name, roll, marks = line.strip().split(",")
                print(f"Name: {name}, Roll: {roll}, Marks: {marks}")
    except FileNotFoundError:
        print("No student records found yet.\n")


# Main program loop
while True:
    print("\n1. Add Student\n2. View Students\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
