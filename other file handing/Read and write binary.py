with open("D:\\python\\other file handing\\binary.txt","w+b") as file:
    file.write(b"Hello, world keowddd!")
    file.seek(0)
    read =file.read()
    print(file)
    print(read)