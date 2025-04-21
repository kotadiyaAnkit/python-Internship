

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

# Push elements onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

print("Current Stack:", stack)

# Peek at the top element (last one added)
print("Top Element:", stack[-1])

# Pop (remove) the top element
popped = stack.pop()
print("Popped Element:", popped)

# Stack after popping
print("Stack Now:", stack)

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
# Output the final state of the stack
print("Final State of Stack:", stack)

