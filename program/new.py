class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        #code 
        if operator ==1:
            print(a + b, end=" ")
        elif operator == 2:
            print(a - b , end=" ")
        elif operator == 3:
            print(a * b ,end=" ")
        else:
            print("Invalid")
            
s1=Solution()
s1.calculate(10, 5, 2)  # Output: 15