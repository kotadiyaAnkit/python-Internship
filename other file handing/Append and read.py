with open("D:\\python\\other file handing\\read and write.txt", "a+") as file:
    file.write("\nNew data added!")  
    file.seek(0)  
    content = file.read()  
    
    print(content)
    
#D:\\python\\other file handing\\read and write.txt