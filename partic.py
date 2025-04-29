a = [1, 2, 3]
b = a 

print(a is b)  

c = [1, 2, 3]
print(a is c) 
#Which of these evaluates to False? ==> 
#ans 0 is 0.0

#What is the value of i in the following code?

word = "banana"
i = word.find("a")
print("banana=>>>>",i)

#What does dict equal after running this code?:

# dict = {"Fri": 20, "Thu": 6, "Sat": 1}
# dict["Thu"] = 13
# dict["Sat"] = 2
# dict["Sun"] = 9

# print(dict)

#What will the following code print?

counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
print(counts.get('kris', 0))


#What will the following code print?:
counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])




#What will the following code print?:

cars = dict()
cars['bmw'] = 1
cars['maruti800'] = 5
cars['swfit'] = 9
for (k,i) in cars.items():
    print(k, i)
    
