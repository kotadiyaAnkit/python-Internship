#Method overriding with multiple and multilevel inheritance
# Python program to demonstrate 
# Defining parent class 1 
class Parent1(): 
		
	# Parent's show method 
	def show(self): 
		print("Inside Parent1") 
		
# Defining Parent class 2 
class Parent2(): 
		
	# Parent's show method 
	def display(self): 
		print("Inside Parent2") 
		
		
# Defining child class 
class Child(Parent1, Parent2): 
		
	# Child's show method 
	def show(self): 
		print("Inside Child") 
	
		
#create a obj of child class
obj = Child() 

obj.show() 
obj.display()

