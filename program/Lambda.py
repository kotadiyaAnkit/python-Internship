x = lambda a : a + 10
print(x(5))

print("-----------------------")

number = lambda a, b: a * b
print(number(5, 6))

print("----------------------")

num = lambda x,y,z : x+y+z
print(num(5, 6, 7))

print("---------------------")
def z(n):
    return lambda z:z+n

total = z(2)

print(total(11))

