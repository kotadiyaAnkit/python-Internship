with open("D:\\python\\other file handing\\read and write.txt","w+") as f:
    write =f.write("Hello world!")
    read = f.read()
    print(read)
    
word="Hello world!"
if(read.find(word)!=-1):
    print("data is found")
else:
    print("data is not found")
        