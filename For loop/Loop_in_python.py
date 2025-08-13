#A list is a collection of items that can be of any type. Here's how you can iterate through a list:
a=[10,20,30,50,60]
for i in a:
    print(i)    

print("---------------------------------------------")

#A string is a sequence of characters. You can iterate through each character in a string as shown below:

s="Hel"
for b in s:
    print(b)

print("---------------------------------------------")

#You can combine the for loop with conditional statements to perform actions based on certain conditions.
# For example, printing numbers that are multiples of 6:

for c in range(20):
    if c % 6 == 0:
        print(c)

print("---------------------------------------------")

## Iterate through a list using index and print each item
l = [10, 20, 30, 40]
for i in range(len(l)):
    print(l[i])
    
print("---------------------------------------------")

#Iterating with Index and Element
#If you need both the index and the element while iterating, you can modify the loop as follows:

d = [1,2,3,4,5]
for e in range(len(d)):
    print(f"Index: {e}, Element: {d[e]}")# e the current index (like a row number)
