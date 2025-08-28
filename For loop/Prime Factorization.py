class Solution:
    def printPrimeFactorization(self, n):
        i=2 #We start  i = 2 because 2 is the small prime number.  dividing n by 2, then 3, then 4, and so .
        factors=[] #empty list to store all the prime factors we find.
        
        while i * i <=n:#This loop runs while i * i is less than or equal to n. check all numbers up to n.
            
            while n % i ==0: #This checks: "Is n divisible by i?"answer yes-> i is a prime factor of n.
                factors.append(i) #We add i to the list of prime factors (because it divides n).
                n//=i#divide n by i used to integer division.
            i+=1 #If n is no longer divisible by i, we go to the next number.
        
        if n>1: #After the loop, if n is still greater than 1, it must be a prime number.->we add it as the last prime factor.
            factors.append(n) #add n to our list of prime factors.
            
        for a in factors: #each number in our factors list...
            print(a, end=' ')
            
        
# def is_prime(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# def print_prime_factors(n):
#     for i in range(2, n + 1):
#         if is_prime(i):
#             x = i
#             while n % x == 0:
#                 print(i)
#                 x = x * i

# n = 100
# print_prime_factors(n)