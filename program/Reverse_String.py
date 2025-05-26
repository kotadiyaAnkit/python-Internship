stack = [] 

for char in "hello":      
    stack.append(char)     

reversed_str = ""
            
while stack:               
    reversed_str += stack.pop()  
    
print(reversed_str) 

    