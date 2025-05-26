# Filter Even Numbers from a List
number = [1,2,3, 4,5,6,7,8,8]

number1 = list(filter (lambda n: n % 2 == 0, number))
print(number1)

print("-----------------------")

#Square Each Number Using map(), Also cube.
first= [1,2,3,4,5]

squran = list(map (lambda b: b**2,first))
print(squran)

print("-------------------------")

# Sort a List of Tuples by Second Value
students = [('Alice', 88), ('Bob', 72), ('Charlie', 95), ('David', 85)]
sorted_stu = sorted(students, key=lambda x: x[1])
print(sorted_stu)