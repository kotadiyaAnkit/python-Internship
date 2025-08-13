# a = [1, 2, 3]
# b = a 

# print(a is b)  

# c = [1, 2, 3]
# print(a is c) 
# #Which of these evaluates to False? ==> 
# #ans 0 is 0.0

# #What is the value of i in the following code?

# word = "banana"
# i = word.find("a")
# print("banana=>>>>",i)

# #What does dict equal after running this code?:

# # dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# # dict["Thu"] = 13
# # dict["Sat"] = 2
# # dict["Sun"] = 9

# # print(dict)

# #What will the following code print?

# counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# print(counts.get('kris', 0))


# #What will the following code print?:
# counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
# for key in counts:
#     if counts[key] > 10:
#         print(key, counts[key])




# #What will the following code print?:

# cars = dict()
# cars['bmw'] = 1
# cars['maruti800'] = 5
# cars['swfit'] = 9
# for (k,i) in cars.items():
#     print(k, i)
    
# #What will the following program print?:
# import re
# s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
# lst = re.findall('\\S+@\\S+', s)
# print(lst)

# my_list = ["a","h","b","c"]
# my_list.reverse
# print(my_list)
# print("------------------------------")     
                   
# list = [1,2,3,4,5]
# list.pop(1)
# print(list)
# print("------------------------------")

# tup= (1,2,3,4)
# tup1 =tup.index(2)
# print(tup1)

# list=[]
# mov =input("Enter a movies name")
# list.append(mov)
# mov =input("Enter a movies name")
# list.append(mov)
# mov =input("Enter a movies name")


# list.append(mov)
# print(list)

#nested dic
# studen = {
#     "name": "John",
#     "subject" :{
#         "math" : 90,
#         "science" : 85,
#         "english" : 95
#     }
# }

# print(len(studen.keys()))

# table={
#     "table" : ["a pice of furnituen","list of facts & figures"],
#     "cat":"a small animal",
    
# }

# print(dict(table.items()))

# set1={"python","java","c++","python","javascript","java","python","java","c++","c"} 

# print(len(set1))

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

factorial(4)