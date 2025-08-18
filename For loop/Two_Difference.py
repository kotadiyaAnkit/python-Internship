#Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line.
#Note: Don't add a new line in the end.

n1 = int(input()) #int() converts that string into an integer. Example: If the user enters 9, then n1 = 9.
n2 = int(input())

result = [str(n1 * i - n2 * i) for i in range(1, 11)] #For each i, we calculate: n1 * i and n2 * i, then subtract them: n1*i - n2*i.


print(" ".join(result))

print("-------------------------------")
n1 = int(input())
n2 = int(input())

table_n1 = [n1 * i for i in range(1, 11)]
table_n2 = [n2 * i for i in range(1, 11)]
diff = [table_n1[i] - table_n2[i] for i in range(10)]

# Print first line: table of n1
print(" ".join(map(str, table_n1))) #Converts the numbers into strings. Joins them with a space " " and prints.

# Print second line: table of n2
print("- " + " ".join(map(str, table_n2)))

# Print separator line
print("-" * 41)

# Print result line: differences
print("= " + " ".join(map(str, diff)), end="")  #Same technique: convert to string, join with space, and add =. end="" makes sure no extra newline is printed at the end.
