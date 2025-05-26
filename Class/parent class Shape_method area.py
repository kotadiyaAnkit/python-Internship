class shape():
    
    def area(self):
        print("Total of a area")
        
class circle(shape):
    def size_circel(self,readuis):
        self.radius = readuis
        self.area = 3.14 * (self.radius ** 2)
        print("Area of a circle is ", self.area)
        
        def area():
            return("Total of a area",shape)
        
        
class rectangle(shape):
    def size_rectangle(self,readuis,readuis2):
        self.length = readuis
        self.width = readuis2
        self.area = self.length * self.width
        print("Area of a rectangle is ", self.area)
        
class square(shape):
    def size_square(self,readuis):
        self.length = readuis
        self.area = self.length * self.length
        print("Area of a square is ", self.area)
        
        
        
circle(4)
rectangle(5,6)
square(7)


    