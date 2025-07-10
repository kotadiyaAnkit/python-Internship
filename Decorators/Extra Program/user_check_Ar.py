users = {
    "admin": "test",
}
def authentication(check): 
    def user():  #user authentication  calling a check
        
        name = input("Enter a name: ") #"Valid User",  calls the check() function (which is check_user().
        if name == users["admin"] :
            print("Valid User")
            check()
        else:
            print("Not user")
    return user

@authentication
def check_user():
    print("Access granted. ")
    
check_user()
    
    