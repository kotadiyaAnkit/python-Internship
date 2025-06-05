class A():
    def first(self, a):
        self.a = a
   
        
class B():
    def first(self, b):
        self.b = b

class C(A, B):
    def show(self):
        print("Class A:",self.a)
        print("Class B:",self.b)
        


c1 = C()

A.first(c1,2)
B.first(c1,3)

c1.show()  # Output: 2 3