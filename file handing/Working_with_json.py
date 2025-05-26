import json

data = {
    "name": "rahul",
    "age": 25,
    "city": "New York"
}

with open("D:\\python\\file handing\\data.json", "w") as file:
    json.dump(data, file, indent=4)
    
print(data)

#Rename a File
#delete a milan load