#User function Template for python3
def is_prime(n):
    if n<=1:
        return False
    if n ==2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3 , int(n**0.5) + 1, 2):  #The loop starts. int(11**0.5) is 3. The range is from 3 to 3 with a step of 2. The loop will only run once for i = 3.
        if n % i ==0: #11 % 3 is 2, not 0. The condition is false. The loop finishes.
            return False
    return True

#back to next_prime
def next_prime(n):
    c = n+1  #c becomes 10 + 1, which is 11.
    while True: #The loop starts.
        if is_prime(c): #The program calls is_prime(11).
             return c #The function returns the current value of c, which is 11.
        c+=1#
        
n = int(input())
print(next_prime(n))