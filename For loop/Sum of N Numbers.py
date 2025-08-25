class Solution:
    def sumOfNumbers(self, n,r):
        n=int(input())
        sum = n * (n + 1) //2
        print(sum)
        
obj = Solution()
obj.sumOfNumbers(5,0)

#Given an integer n find the sum of the first n natural number.

class Solution:
    def natural_number(self, a):
        return a * (a+1) //2
    
s1 = Solution()
print(s1.natural_number(5))

