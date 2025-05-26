contant={
    "rahul" : 8274847,
    "amit": 82023948,
    "raj" : 8729473
}

#ADD USER 
contant["meet"] = 87348762

#update user

contant.update({"amit": 2020})
print("--------------------------")

#serach
user = input("Enter a name to search: ")

# Check if name exists in the dictionary
if user in contant:
    print(user, "message :", contant[user])
else:
    print(" not found.")

contant.pop("raj")

print(contant)

