class Preson():
    def first(self):
        print("first class")
    
class b(Preson):
    def secound(self):
        print("secound class")
        
class c(Preson):
    def thrid(self):
        print("thrid class")
        
class d(c, b):
    def fourth(self):
        print("four class")
    
A1 = Preson()
A2 = b()
A3 = c()
A4 = d()

A4.first()
A4.secound()
A4.thrid()
A4.fourth()