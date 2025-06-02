class Employee:
    def __init__(self, name, age, salary, year):
        self.name = name
        self.age = age
        self.salary_amount = salary  
        self.year = year

    def get_salary(self):
        return self.salary_amount
    
    def get_year(self):
        return self.year


class FullTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours, year):
        super().__init__(name, age, salary,year)
        self.hours = hours

    def get_salary(self):
        return self.salary_amount * self.hours
    
    def get_year(self):
        return self.salary_amount * 60


class PartTimeEmployee(Employee):
    def __init__(self, name, age, salary, hours, year):
        super().__init__(name, age, salary, year)
        self.hours = hours

    def get_salary(self):
        return self.salary_amount * self.hours
    
    def get_year(self):
        return self.salary_amount * 60


full_time = FullTimeEmployee("Milan", 20, 2200, 3, 2)
print("Full-time salary:", full_time.get_salary())
print("year", full_time.get_year())

part_time = PartTimeEmployee("Meet", 23, 400, 4, 3)
print("Part-time salary:", part_time.get_salary())
print("year", part_time.get_year())
