#First, let's start with a basic program that generates the multiplication table for a given number n. This program will print the first 10 multiples of n.
n = int(input("Enter a number to generate its multiplication table: "))
i = int(input("Enter the range for the multiplication table (default is 10): "))
for i in range(1, 11):
    print(n * i, end=" ")

print("\n---------------------------------------------")
#Extended Multiplication Table with User-Specified Length Using while Loop
#Next, let's extend the program to allow the user to specify how many multiples they want to print.

a=5
b=7
c=1

while c<=b:
    print(a*c, end=" ")
    c+=1