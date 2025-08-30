number = 12
print("Binary equivalent:", bin(number)[2:])

#Other method binary conversion without using bin() function
def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary  #Prepend the remainder (0 or 1) to the binary string
        n = n // 2                     #Update n to be n divided by 2 (integer division)
    return binary
n = 23
print("Binary equivalent (without using bin()):", decimal_to_binary(n))