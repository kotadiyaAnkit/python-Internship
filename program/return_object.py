#Use __str__ Method to return object from a class & print it.

class preson:

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age})"
        
        
preson1 =preson("alic",30)

print(preson1.name)
print(preson1.age)


        