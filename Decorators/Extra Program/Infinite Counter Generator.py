def infinite_counter():
    num = 0  # Start from 0
    while True:  # Infinite loop
        yield num  # Yield the current number
        num += 1  # Increment the number

# Example usage
for count in infinite_counter():
    print(count)
    if count >= 10:  # Stop after 10 iterations (to avoid infinite loop in practice)
        break


# def infinite_counter():
#     num = 0
#     while True:
#         yield num
#         num += 1

# # Example usage
# counter = infinite_counter()
# print(next(counter))  # Output: 0
# print(next(counter))  # Output: 1
# print(next(counter))  # Output: 2
