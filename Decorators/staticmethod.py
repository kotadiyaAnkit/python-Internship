class sum:
    @staticmethod
    def add(a, b):
        return a + b

# Call the static method using the class name (no object needed)
result = sum.add(5, 3)
print("Sum:", result)
