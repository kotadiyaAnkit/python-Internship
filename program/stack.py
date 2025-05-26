

# # Stack size
# SIZE = 5
# stack = []
# top = -1

# # Push operation
# def push():
#     global top
#     if top < SIZE - 1:
#         value = int(input("Enter any value: "))
#         stack.append(value)
#         top += 1
#         print(f"{value} pushed to stack.")
#     else:
#         print("Stack is full.")

# # Pop operation
# def pop():
#     global top
#     if top == -1:
#         print("Stack is empty.")
#     else:
#         print(f"{stack[top]} is deleted...")
#         stack.pop()
#         top -= 1

# # Display operation
# def display():
#     if top == -1:
#         print("Stack is empty.")
#     else:
#         print("Stack elements from top to bottom:")
#         for i in range(top, -1, -1):
#             print(f"\t{stack[i]}")

     
# # Menu-driven program
# def main():
#     while True:
#         print("\n1. Push")
#         print("2. Pop")
#         print("3. Display")
#         print("4. empty")
#         print("0. Exit")
        
#         try:
#             choice = int(input("Enter your choice: "))
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             continue

#         if choice == 1:
#             push()
#         elif choice == 2:
#             pop()
#         elif choice == 3:
#             display()
#         elif choice == 0:
#             print("Exiting...")
#             break
#         else:
#             print("Please enter a valid choice (0 to 3).")

# # Run the program
# main()
# Create an empty stack

stack = []

stack.append(8)
stack.append(9)
stack.append(10)

print("Current Stack:", stack)

#(last one added)
print("Top Element:", stack[-1])

#(remove)
popped = stack.pop()
print("Popped Element:", popped)


print("Stack Now:", stack)

if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")

print("Final State of Stack:", stack)

