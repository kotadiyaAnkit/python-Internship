# Predefined form submissions (as tuples)
form1 = ("milan", "milan@gmail.com", "bca")
form2 = ("delhi", "delhi@gmail.com", "bca")

# Store forms in a set (set of tuples)il
collection = {form1, form2}

# Input from user
name = input("Enter a name: ")
email = input("Enter an email ID: ")
stream = input("Enter a stream: ")

# Pack user input into a tuple
submit = (email)

# Check if the 
if submit in collection:
    print("Already logged.")
else:
    print("Not Ready.")
