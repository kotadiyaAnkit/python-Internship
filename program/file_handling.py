

#write data in file
file = open("C:\\Users\\Ankit Kotadiya\\Desktop\\my file\\ak-5\\a.txt","w")
a=file.write("Hello, World!")
a=file.write("i am learn about python")
print(a)
file.close()

# Read Lines
with open("C:\\USers\\Ankit Kotadiya\\Desktop\\my file\\ak-5\\a.txt","r") as a:
  print(a.read())



    