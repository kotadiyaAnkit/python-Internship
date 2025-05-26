#Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil","")

print("----------------------------")

#Arbitrary Arguments, *other name
def Arbitrary(*kids):
  print("The youngest child is " + kids[2])

Arbitrary("Emil", "Tobias", "Linus")

print("----------------------------")

#Keyword Arguments
def keyword(child3, child2, child1 , child4):
    print("The youngest keyword is " + child3)
    
keyword(child1 = "Emil", child2 = "Tobias", child3 = "hello" , child4 = "book")

