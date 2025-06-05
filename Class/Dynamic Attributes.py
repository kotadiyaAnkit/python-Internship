class preson():
    def __init__(self, name):
        self.name = name
        
p = preson("ak")
p.age = 22  #dynamic attribute 

print(p.name)
print(p.age)
print("\n")

#explain this program 
class OuterClass:
    def __init__(self):
        self.title = "Main Class" 

    class FirstClass:
        def __init__(self):
            self.name = "First Level"

        class SecondClass:
            def __init__(self):
                self.label = "Second Level"

# Create objects
outer = OuterClass()
first = OuterClass.FirstClass()
second = OuterClass.FirstClass.SecondClass()

# Add dynamic attributes
outer.aa = "1.0"
first.description = "This is the first inner class"
second.code = "XYZ123"

# Print dynamic attributes
print("Outer Title:", outer.title)
print("Outer Version (dynamic):", outer.aa)

print("First Name:", first.name)
print("First Description (dynamic):", first.description)

print("Second Label:", second.label)
print("Second Code (dynamic):", second.code)
