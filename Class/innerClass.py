class Color:
    def __init__(self):
        self.name = 'Green'
        self.l = self.Lightgreen(self)

    def show(self):
        print('Name:', self.name)
        
    def access_child(self):
        print("Accessing child class from parent class:")
        self.l.display()  # Accessing child class method

    class Lightgreen:
        def __init__(self,c1):
            self.name = 'Light Green'
            self.code = '024avc'
            self.Color = c1

        def display(self):
            print('Name:', self.name)
            print('Code:', self.code)
            self.Color.show()

c = Color()
c.access_child()
# outer = Color()
# outer.show()


# inner = outer.l
# inner.display()
# g = outer.l

# # inner class method calling
# g.display()

print("\n")


# # create outer class
# class Doctors:
#     def __init__(self):
#         self.name = 'Doctor'
#         self.den = self.Dentist()
#         self.car = self.Cardiologist()

#     def show(self):
#         print('In outer class')
#         print('Name:', self.name)

#     # create a 1st Inner class
#     class Dentist:
#         def __init__(self):
#             self.name = 'Dr. Savita'
#             self.degree = 'BDS'

#         def display(self):
#             print("Name:", self.name)
#             print("Degree:", self.degree)

#     # create a 2nd Inner class
#     class Cardiologist:
#         def __init__(self):
#             self.name = 'Dr. Amit'
#             self.degree = 'DM'

#         def display(self):
#             print("Name:", self.name)
#             print("Degree:", self.degree)


# # create a object
# # of outer class
# outer = Doctors()
# outer.show()

# create a object
# of 1st inner class
# d1 = outer.den

# # create a object
# # of 2nd inner class
# d2 = outer.car
# print()
# d1.display()
# print()
# d2.display()