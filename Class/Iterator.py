# This code snippet is creating an iterator object from a list `['Geeks', 'For', 'Geeks']` using the
# `iter()` function. Then, it is using the `next()` function to iterate over the elements of the
# iterator and print them one by one.

#Iterators 
iter_list = iter(['Geeks', 'For', 'Geeks'])
print(next(iter_list))
print(next(iter_list))
print(next(iter_list))

#Generators
def sq_numbers(n):
    for i in range(1, n+1):
        yield i*i


a = sq_numbers(3)

print("The square of numbers 1,2,3 are : ")
print(next(a))
print(next(a))
print(next(a))

