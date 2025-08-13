import pytest
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
select  = input("Enter operator (1, 2, 3, 4): ")

# Check operator 
if select == '1':
    print("Result:", add(a, b))
elif select == '2':
    print("Result:", subtract(a, b))
elif select == '3':
    print("Result:", multiply(a, b))
elif select == '4':
    if b == 0:
        print("Error: Cannot divide by zero")
    else:
        print("Result:", divide(a, b))
else:
    print("Invalid operator")
