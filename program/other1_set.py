# Clear a set
my_set = {10, 20, 30, 40}

# Clear the set
my_set.clear()

print("Cleared set:", my_set)

#Find symmetric difference (elements in either set, but not both)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x ^ y  
a=x.difference(y)

print(a)
print("-------------------------")
print(z) 


import json
data = '''
  [
    { "id" : "001",
      "x" : "2",
     "name" : "Quincy"
    } ,
    { "id" : "009",
      "x" : "7",
      "name" : "Mrugesh"
    }
  ]
'''
info = json.loads(data)
print(info[1]['name'])