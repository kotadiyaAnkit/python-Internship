
try:
    file = open("binar.txt", "r")
    content = file.read()
    print(content)
    file.close()
except FileNotFoundError:
    print("The file does not exist!")
    
    #D:\\python\\other file handing\\binary.txt