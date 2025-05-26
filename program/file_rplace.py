# with open("myfile.txt","w") as h:
#     print(h.write("hi everone\npratic to java file handing"))  
#     print(h.write("\nmy name to milan\nand to laring about java"))
    
# replace the data
# with open("myfile.txt","r") as h:
#     data= h.read()
    
#     new=data.replace("java","python")
#     print(new)
    
# with open("my file.txt","w") as h:
#     h.write(new)
    
#find the data
def checkword():
        word="to"
        with open("my file.txt","r") as h:
         data= h.read()
        if(data.find(word)!=-1):
            print("data is found")
        else:
            print("data is not found")
        
checkword()