n = int(input())


def fibonacci(n):
    if n==0: #The First number is defined as 0
        return 0 #if the input is 0, return 0.
    a,b = 0,1#First two  fibonacci numbers F(0) = 0, F(1) = 1
    
    for _ in range(2 , n+1): #This loop runs from 2 to n , What used form 2? Because we already have F(0) and F(1).
        
        a,b = b, a+b # A calculate the next number: F(n) = F(n-1) + F(n-2) And update a and b. A is new And B is old,
    return b

fib = fibonacci(n) 
print(fib)


#Initial a = 0, b = 1

#Iteration 2: a = 1, b = 1

#Iteration 3: a = 1, b = 2 

#Iteration 4: a = 2, b = 3
#Iteration 5: a = 3, b = 5