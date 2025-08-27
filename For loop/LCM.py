#A more efficient way to calculate the LCM is by using the Greatest Common Divisor (GCD). The relationship between LCM and GCD is:


#LCM (a, b) = |a * b| / GCD(a, b)

import math

a = int(input())
b = int(input())
gcd = math.gcd(a, b) # The math.gcd() function efficiently finds the largest positive integer that divides both a and b without a remainder.

lcm = (a * b) //gcd #The fundamental relationship between LCM and GCD is LCM(a, b) = (a * b) / GCD(a, b).
print(lcm)

#easy Method
def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a = int(input())
b = int(input())