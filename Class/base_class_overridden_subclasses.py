# class animal():
#     def speak(self):
#         print("animal sound animal")
        
    
# class dog(animal):
#         def speak(self):
#             print("woof")
        
# class cat(animal):
#         def speak(self):
#             print("meow")
        
# a = Animal
# d = Dog
# c = Cat

# print(a.speak())  # Output: Some generic animal sound
# print(d.speak())  # Output: Woof! Woof!
# print(c.speak())

class Animal:
    def speak(self):
        print ("Some generic animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow! Meow!")

# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Calling the overridden method
a.speak()

print(d.speak()) 
print(c.speak())  



                