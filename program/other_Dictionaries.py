#Change Values
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018
print(thisdict)

#update 
student = {
  "name": "Rahul",
  "stream": "Bca",
  "year": 1964
}

student.update({"year": 2020})
print(student)
print("-----------------------")

#Adding Items
thisdic = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdic["color"] = "red"
print(thisdic)

#remove
dict1 = {
        1: "name",
        2: "age",
        3: "study"
            }
dict1.pop(2)
# car.popitem() remove to last element
# del dict1[1]
print(dict1)

print("----------------------------")


#all the value print with loop
fruits={
    "name": "apple",      #name = key and apple=values
    "name2": "banana",
    "name3": "orange"
}

#print a all items
for x in fruits:
  print(x)

#print a valus is keys  
# for x in fruits.keys():
#   print(fruits[x])
  
# for x in fruits.items():
#   print(fruits)
#   print("\n---------------------------") 
  
  
#Copy a Dictionary
a = {
  "stream": "Ford",
  "stream2": "Mustang",
  "stream3": 2001
}
mydict = a.copy()
print(mydict)

print("--------------------------------")

#nested 
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print("\t",myfamily)

print("------")


#Access Items in Nested Dictionaries
print(myfamily["child2"]["name"])
#Access child2 show all item
print(myfamily["child2"])