class Solution:
    def print_even_indices(self, s: str):
        for i in range(0, len(s), 2):
            print(s[i], end="")

s1 = Solution()
s1.print_even_indices("Geeks")  # Output: Gks
print("\n---------------------------------------------")

x = int(input("Enter a number: "))
while x >= 0:
    print(x, end=" ")
    x -= 1

print("\n---------------------------------------------")

x = "GFG"
for i in range(len(x)):
    print(f"Index {i}: {x[i]}")
