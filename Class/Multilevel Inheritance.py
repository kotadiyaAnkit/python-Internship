class BaseClass:
    def first(self):
        print("BaseClass method")

class ParentClass(BaseClass):
    def second(self):
        print("ParentClass method")

class ChildClass(ParentClass):
    def third(self):
        print("ChildClass method")

class MainClass(ChildClass):
    def display(self):
        print("MainClass method")

# Creating an object of MainClass which has access to all inherited methods
obj = MainClass()
obj.first()  
obj.second()  
obj.third()  
obj.display()  
