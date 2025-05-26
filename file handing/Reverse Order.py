file_pat="D:\\python\\file handing\\students.txt"
with open(file_pat,"r") as file:
    data = file.read()
    reversed_file=data[::-1]
    print(reversed_file)

