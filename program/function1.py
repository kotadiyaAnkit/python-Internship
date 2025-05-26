#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

print("--------------------------------------")

#Default Parameter Value
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("10")
my_function()
my_function("Brazil")

print("--------------------------------")

#Passing a List as an Argument
def Passing(food):
    for x in food:
        print(x)
        
frusit=["apple","banana","mango"]
Passing(frusit)
print("--------------------------------")

