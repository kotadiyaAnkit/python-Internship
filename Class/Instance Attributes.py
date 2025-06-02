#Class and Instance Attributes in Python
class sum():
    count = 0
    
    def sec_time(self):
        sum.count +=1
        
s1 = sum()
s1.sec_time()
print(s1.count)

s1 = sum()
s1.sec_time()
print(s1.count)

print(sum.count)
print("\n")


# Python program to demonstrate
# instance attributes.
class emp:
    def __init__(self):
        self.name = 'xyz'
        self.salary = 4000

    def show(self):
        print(self.name)
        print(self.salary)

e1 = emp()
print("Dictionary form :", vars(e1))
print(dir(e1))