class Solution:
    def findPreviousDay(self, d: int, n: int) -> int:
        # (d - n) % 7 ensures the result stays within 0-6
        return (d - n) % 7
if __name__ == "__main__":
    d = int(input("Enter current day index (0-6): "))
    n = int(input("Enter number of days before: "))
    sol = Solution()
    print("Day index", n, "days before day", d, "is:", sol.findPreviousDay(d, n))
