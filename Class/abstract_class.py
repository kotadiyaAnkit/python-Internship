# class Vehicle():
#     @staticmethod
#     def start_engine(self):
#         print("start engine")
        
# class car(Vehicle):
#     @staticmethod
#     def start_engine(self):
#         print("start car engine")
        
# class Bike(Vehicle):
#     @staticmethod
#     def start_engine(self):
#         print("start bike engine")
    
    
# Vehicle.start_engine()
# car.start_engine()
# Bike.start_engine()

class Vehicle:
  
    def start_engine():
        print("Start engine")

class Car(Vehicle):

    def start_engine():
        print("Start car engine")

class Bike(Vehicle):

    def start_engine():
        print("Start bike engine")


Vehicle.start_engine()  
Car.start_engine()      
Bike.start_engine()     






