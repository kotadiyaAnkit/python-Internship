class Solution:
    def binaryToDecimal(self, b):
        return int(b, 2) #int(b, 2) tells Python to convert the string b (which is in base-2) into a base-10 integer.
    #int("111", 2) → 7
    #int("1010", 2) → 10
    #int("100", 2) → 4

s1 = Solution()
print(s1.binaryToDecimal("111"))
print(s1.binaryToDecimal("1010"))