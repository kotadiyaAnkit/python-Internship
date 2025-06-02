class preson():
    
    def __init__(self,name):
        self.name = name
        
        
p1 = preson("rahul")
print(p1.name)
print("\n")


#Class and Instance Variables in Python
class student():
    school_name = "xyz"
    
    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name
    

c1 = student(111,"milan")
print(c1.rollno)
print(c1.name)
print("\n")


c1.name = "rahul"
print(c1.name)

student.school_name = "python"
print(student.school_name)