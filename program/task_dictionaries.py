# student = {
#     "milan": "A+",
#     "bhavin": "C",
#     "meet": "D"
# }
# marks = int(input("Entrer a marks:"))
# if(marks>=90):
#     print("Grand A")
# elif(marks>=80 and 90<=marks):
#     print("Grand B")
# elif(marks>=70 and 80<=marks):
#     print("Grand c")
# else:
#     print("Grand D")

# if marks in student:
#     print("Quantity of", marks, "is", student)
# else:
#     print(marks, "not found in inventory.")    

# name = input("Enter a name: ")

# if name in student:
#     print(name, " grade", student[name])
    
# elif(name!=student):
#     print("Not found")



# Dictionary of students and their grades
student = {
    "milan": "A+",
    "bhavin": "C",
    "meet": "D"
}

# Input marks
marks = int(input("Enter marks: "))

# Grade calculation
if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
else:
    print("Grade D")

# Show  (keys)
print("\nList of students:")
for name in student.keys():
    print(name)

# Show  (values)
print("\nList of grades:")
for grade in student.values():
    print(grade)
 
# Show specific student's grade
name_input = input("\nEnter student name to see grade: ")
if name_input in student:
    print(name_input, "got grade", student[name_input])
else:
    print("Student not found.")
