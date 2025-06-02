# First product method.
# Takes two argument and print their
# product


def product(a, b):
    p = a * b
    print(p)

# Second product method
# Takes three argumenta and print their
# product


def product(a, b, c):
    p = a * b*c
    print(p)

# Uncommenting the below line shows an error
# product(4, 5)


# This line will call the second product method
product(4, 5, 5)


# Python program to demonstrate 
# Python program to demonstrate 
# overriding in multilevel inheritance 

class Parent(): 
		
	# Parent's show method 
	def display(self): 
		print("Inside Parent") 
	
	
# Inherited or Sub class (Note Parent in bracket) 
class Child(Parent): 
		
	# Child's show method 
	def show(self): 
		print("Inside Child") 
	
# Inherited or Sub class (Note Child in bracket) 
class GrandChild(Child): 
		
	# Child's show method 
	def show(self): 
		print("Inside GrandChild")		 
	
# Driver code 
g = GrandChild() 
g.show() 
g.display()