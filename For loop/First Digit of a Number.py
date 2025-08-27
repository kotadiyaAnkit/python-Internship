def firstDigit(n):
    n =abs(n)
    while n >=10:
        n//=10
    return n

print(firstDigit(1234))