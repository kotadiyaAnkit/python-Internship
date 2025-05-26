class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
        
    def get_aver(self, averged):
        sum = self.mark
        aver = sum/3
        return aver
        
        

s1 = Student("jack", [99, 88, 88])
print(s1.name, s1.mark)  # Output: jack [99, 88, 88]


