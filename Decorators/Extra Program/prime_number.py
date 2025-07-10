def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Only check up to √n
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
    for num in range(2, limit + 1):
        if is_prime(num):
            yield num
for prime in prime_generator(100):
    print(prime)

