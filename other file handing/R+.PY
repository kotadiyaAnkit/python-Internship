with open("D:\\python\\other file handing\\read and write.txt","r+") as f:
    read = f.read()
    write = f.write("my name is ak")
    print(read)
    print(write)