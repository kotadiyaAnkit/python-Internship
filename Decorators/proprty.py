class Solution:
    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c

    def printValues(self, a, b,c):
       self.a = a
       self.b = b
       self.c = c
       print(self.a)
       print(self.c)
        
sol = Solution(5, 6, 15)
sol.printValues(5, 6, 15)
