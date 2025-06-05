class car():
    def __init__(self, name):
        self.name = name
        
    def start(self):
        raise NotImplementedError ("Subclass must implement abstract method")
        
class electric_car(car):
    
    def sound(self):
        
        return "car is start"
    
c = car("xyz")
c.start

print(c.name)

e = electric_car("asd")
c.start
print(e.name)

print(e.sound())

    