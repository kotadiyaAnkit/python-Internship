
#program 3

# inventory = {
#     "oil": {"price": 2.5, "quantity": 10},
#     "pen": {"price": 1.2, "quantity": 20},
#     "shampo": {"price": 1.8, "quantity": 15}
# }

# #ADD USER 
# inventory["notebook"] = {"price": 3.0, "quantity": 50}

# print("-------------------------------")


# #update 
# # inventory["oil"]["price"]= 3.0
# inventory["oil"]["quantity"]= 2

# # Inventory dictionary
# inventory = {
#     "oil": {"price": 2.5, "quantity": 10},
#     "pen": {"price": 1.2, "quantity": 20},
#     "shampo": {"price": 1.8, "quantity": 15}
# }

# # Ask for item name
# item = input("Enter item name: ")

# # Show quantity
# if item in inventory:
#     print("Quantity of", item, "is", inventory[item]["quantity"])
# else:
#     print(item, "not found in inventory.")
# print(inventory)




# Initial inventory
inventory = {
    "oil": {"price": 2.5, "quantity": 10},
    "pen": {"price": 1.2, "quantity": 20},
    "shampo": {"price": 1.8, "quantity": 15}
}

print("-------------------------------")

# Add new item from user input
item_name = input("Enter new item name to add: ")
item_price = float(input(f"Enter price for {item_name}: "))
item_quantity = int(input(f"Enter quantity for {item_name}: "))

inventory[item_name] = {"price": item_price, "quantity": item_quantity}

print(f"{item_name} added to inventory.")

print("-------------------------------")

# Ask user for item name to check quantity
item = input("Enter item name to check quantity: ")

# Show quantity
if item in inventory:
    print("Quantity of", item, "is", inventory[item]["quantity"])
else:
    print(item, "not found in inventory.")
