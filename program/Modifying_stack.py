def mod_stack(s):
    stack = []
    
    while s:
        item = s.pop()
        print(item)
        stack.append(item)
    
    # real stack
    while stack:
        s.append(stack.pop())

# Exampl
my_stack = [1, 2, 3, 4, 5]

# Call a function
mod_stack(my_stack)

# real
print("After printing:", my_stack)