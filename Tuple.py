# Using Built-in Function
tup = tuple("milan")
print(tup)


#Demonstrates how to correctly define a tuple with only one element.
tuple = (1,)
print(tuple)

#Tuple Concatenation
tuple = (1,2,3,4)
tuple1 = (5,6,7,8,)
tuple2 = ('qwewe','lion')

a = tuple+tuple1+tuple2
print(a) 

# multipal time a print a value
tup1 = ('boy',) * 3
print(tup1)

#Checks whether a specific item is present in the tuple.

tuple3 = ("a","b","c")
print("a" in tuple3)
print("d" in tuple3)

#Tuple Slicing- Prints a portion of the tuple using slicing.
tuple4 = (10,20,30,40,50)
slice= tuple4[1:4]
print(slice)

# # Slicing of a Tuple with Numbers
# tup = tuple('GEEKSFORGEEKS')

# # Removing First element
# print(tup[1:])

# # Reversing the Tuple
# print(tup[::-1])

# # Printing elements of a Range
# print(tup[4:9])



number = int(input("Enter a numeber:"))
number1 = int(input("Enter a numeber:"))
number2 = int(input("Enter a numeber:"))

if(number>=number1):
    print("bifg",number)
elif(number1>=number2):
    print("big value",number1)
elif(number2>=number):
    print("bbig",number2)