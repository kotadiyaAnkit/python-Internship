try:
    Permission_file = open("D:\\python\\other file handing\\binary.txt", "w")
    Permission_file.write("Top secret information!")
    Permission_file.close()
except PermissionError:
    print("You don't have permission to write to this file!")    