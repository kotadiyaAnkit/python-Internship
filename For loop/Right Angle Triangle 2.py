# class Solution:
#     def printPattern(self, n):
#         for i in range(1, n+1):
#             if i == 1:
#                 print("*")
#             elif i == n:
#                 print("*" * n)
#         else:
#             print("*" + " " * (2 * i - 3) + "*")
    
# obj = Solution()
# obj.printPattern(4)


class Solution:
    def printPattern(self, n):
        for i in range(1, n+1):
            if i == 1:
                print("*") # prints a single asterisk. This forms the apex of the triangle.
                
            elif i == n: #This condition is true only for the last row (when i is 9).
                print("* " * n)  # Adds space between stars
                
            else: #This block handles all the middle rows (from i = 2 to i = 8).
                print("*" + " " * (2 * i - 3) + "*")  # " " * (2 * i - 3) calculates and prints the number of spaces between the two asterisks. The number of spaces increases with each row.

        #For i = 2: 2 * 2 - 3 = 1 space.
        #For i = 3: 2 * 3 - 3 = 3 spaces.

# Example usage:
s1 = Solution()
s1.printPattern(9)

