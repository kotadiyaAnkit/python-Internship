with open("D:\\python\\file handing\\students.txt","r") as c:
    other_file=c.read()
    print(other_file)
    
with open("D:\\python\\file handing\\mark.txt","w") as d:
    d.write(other_file)
    print(d)