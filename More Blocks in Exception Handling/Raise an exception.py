def age():
  try:
    check_age=int(input("Enter a age "))
    if (check_age<18):
        raise ValueError("Age cannot be")
    print("This Age Is valid")
    print(age) 
  except ValueError as get_age:
        print(f"That is : {get_age}")
        
age()
        
    
    