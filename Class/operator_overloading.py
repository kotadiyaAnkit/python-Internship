class operator_oveloadinf():
    def __init__(self, a,b):
        self.a = a
        self.b = b
        

    def __add__ (self,other):
       return self.a+ other.a,  self.b + other.b
    
o1 = complex(2,3)
o2 = complex(4,5)
o3 = o1+o2
print(o3)