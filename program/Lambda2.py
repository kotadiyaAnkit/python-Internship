# Extract Names Starting with 'A'
name=["darshil","ajay","jack","ankit"]

filter1= list(filter(lambda n:n.startswith("a"),name))

print(len(filter1))
print(filter1)

print("-----------------------")

#Multiply Elements by Their Index
numbers=[1,2,3,4,5]

multiply_num = list(map(lambda n:n*numbers.index(n),numbers))
print(multiply_num)

print("----------------------------")


