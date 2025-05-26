#Difference of two sets
a={10,20,30}
b={30,40,50}


c =a.difference(b)
print(c)


#Intersection of two sets
number={1,2,3,4,5}
number2={6,7,8,9}

Intersection  = number|number2


#Check if a value exists in a set
check = int(input("Enter a number"))

if check in Intersection:
    print("is in intesection")
else:
    print("this not found")
print(Intersection)


#Loop through a set & access and print them all
set ={10,20,30,40,50}

for x in set:
    print(x)
    


