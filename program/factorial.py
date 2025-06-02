def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))


#other method used to recursion

def recusion(a):
    if a == 0 :
        return 1
    else:
        return a*recusion(a-1)

print(recusion(3))

# n=6
# fast = 1

# for  i in range(1,n+1):
#     fast *= i
#     break
#     print(fast)
    