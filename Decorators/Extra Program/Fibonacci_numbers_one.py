def fibonacci(limit):  #limit — the maximum value we want in the Fibonacci series.
    a = 0
    b = 1
    while a <= limit:  #a is less than or equal to the limit, we continue generating numbers.
        yield a    # a to the caller (outside the function) 
        a, b = b, a + b #update a value


for num in fibonacci(50):
    print(num)
