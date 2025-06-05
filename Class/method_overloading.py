# Python program to demonstrate 
# Defining parent class 1 
class Parent1(): 
		
	# Parent'
	def show(self): 
		print("Inside Parent1") 
		
# Defining Parent class 2 
class Parent2(): 
		
	# Parent'
	def display(self): 
		print("Inside Parent2") 
		
		
# child class 
class Child(Parent1, Parent2): 
		
	# Child's  
	def show(self): 
		print("Inside Child") 
	
		
# Driver's code 
obj = Child() 

obj.show() 
obj.display()
