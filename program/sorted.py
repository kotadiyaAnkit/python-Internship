
#list
numbers = [5, 1, 8, 3, 10, 4,8]

#Remove duplicates Data
unique_numbers = list(set(numbers))

#find a second value
if len(unique_numbers) < 2:
    print("Not enough unique numbers to find second largest.")
else:
    
    unique_numbers.sort()
    
   
    second_largest = unique_numbers[-2]
    print("Second largest number is:", second_largest)
 
 
 