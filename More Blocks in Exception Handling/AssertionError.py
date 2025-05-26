# age = int(input("Enter your age: "))
# if age <= 0:
#     raise AssertionError("Age must be 0 or greater") 
# print("Valid age!")


try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise AssertionError("Age must be non-negative")
    print("Age is valid.")
except AssertionError as e:
    print("Assertion failed:", e)

# try:
#     assert 2 + 2 == 5, "Math is broken"
# except AssertionError as e:
#     print("Assertion failed:", e)

