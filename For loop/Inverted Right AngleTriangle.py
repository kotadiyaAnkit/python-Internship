class Solution:
    def printPattern(self, n):
        n=9
        for i in range(n, 0, -1):
            print('* ' * i)
            
set = Solution()
set.printPattern(4)