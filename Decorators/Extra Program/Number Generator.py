def even_number_generator(limit):
    for num in range(limit + 1):  #num = 0
        if num % 2 == 0:  #check a number
            yield num  #sends one even number at a time.

# Example usage
for even in even_number_generator(20):
    print(even) 
