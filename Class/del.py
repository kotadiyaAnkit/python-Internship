# Python program to illustrate destructor
 
class Employee:
 
    # Initializing
    def __init__(self):
        print('Employee created 3')
 
    # Calling destructor
    def __del__(self):
        print("Destructor called5")
 
def Create_obj():
    print('Making Object.2.')
    obj = Employee()
    print('function end...4')
    return obj
 
print('Calling Create_obj() function..1')
obj = Create_obj()
print('Program End...')