# Assigning a function to a variable
def greet(n):
    return f"Hello, {n}!"

say_hi = greet     # Assign the greet function to say_hi      greet -> say_hi
print(say_hi("Alice"))  

# Passing a function as an argument
def apply(f, v):  #f: a function (here, say_hi) and v: a value (here, "Bob")
    return f(v)

res = apply(say_hi, "Bob")
print(res)  

# Returning a function from another function
def make_mult(f):
    def mult(x):
        return x * f
    return mult

dbl = make_mult(2)  #  to call  the make_mult(2)
print(dbl(5))   #dbl(5) becomes 5 * 2 → 10