class Solution:
    def lastDigit(self, n: int) -> int:  #-> int: This indicates that the function returns an integer.
        return int(str(n)[-1]) # Gets the last character of the string.

#[-1] is Python's way of saying "last element".

# This is a Python convention to run code only if the file is being executed directly (not imported as a module).
if __name__ == "__main__":
    n = int(input())
    sol = Solution()
    print(sol.lastDigit(n))
