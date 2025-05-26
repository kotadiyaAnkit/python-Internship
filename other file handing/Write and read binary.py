with open("D:\\python\\other file handing\\binary.txt", "w+b") as file:
    file.write(b"Hello binary world!")
    file.seek(0)        
    data = file.read()
    print(data)

