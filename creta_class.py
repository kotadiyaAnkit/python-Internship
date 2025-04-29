#  class
# class a:
#     s = "hello"  



# d1 = a()

# print(d1.s)

class b:
    species = "Canine"  # Class

    def __init__(self, name, age):
        self.name = name  
        self.age = age  
        
    def __str__(self):

        return f"{self.name} is {self.age} years old."   
    
# object
d1 = b("Buddy", 3)
d2 = b("Age",30)


# print(d1.age)# buddy
# print(d2.name)







