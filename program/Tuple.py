# Using Built-in Function
tu = tuple("milan")
print(tu)


#Demonstrates how to correctly define a tuple with only one element.
tup = (1,)
print(tup)

#Tuple Concatenation
tupl = (1,2,3,4)
tuple1 = (5,6,7,8,)
tuple2 = ('qwewe','lion')

a = tupl+tuple1+tuple2
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



    
def doubleTup(numbers):
    return tuple(num * 2 for num in numbers)

tup = (4, 5, 1, 2, 3, 5)
print(doubleTup(tup))  # Output: (8, 10, 2, 4, 6, 10)
