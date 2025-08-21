#You are given a string s, you need to print its characters at even indices (index starts at 0).
class Solution:
    def print_even_indices(self, s: str):
        #code here
        for i in range(0, len(s), 2):
            print(s[i],end="")
  
s1 = Solution()
s1.print_even_indices("Geeks")  # Output: Hlool
print("\n---------------------------------------------")

x = int(input())
while x >=0:
    print(x, end=" ")
    x-=1
    
x="GFG"

for i in range(x):

    print(i)