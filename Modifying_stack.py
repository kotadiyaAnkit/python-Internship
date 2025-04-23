def mod_stack(s):
    stack = []
    

    while s:
        item = s.pop()
        print(item)
        stack.append(item)
    
    # Real number 
    while stack:
        s.append(stack.pop())

# Ex
mod_stack = [1, 2, 3, 4, 5]  #   top =5
mod_stack(mod_stack)
print("After printing:", mod_stack)