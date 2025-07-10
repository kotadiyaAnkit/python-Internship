class Employee:
    count = 0  # Class variable to track number of employees

    def __init__(self, name):
        self.name = name
        Employee.count += 1

    @classmethod
    def how_many_employees(cl):
        print(f"Total Employees: {cl.count}")
        
e1 = Employee("jack")
e2 = Employee("Bob")
Employee.how_many_employees()   
