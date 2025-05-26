import os

#D:\python\file handing\mark.txt
old_name = 'D:\\python\\file handing\\copy_file.txt'
new_name = 'D:\\python\\file handing\\mark.txt'


rename= os.rename(old_name, new_name)

print(rename)

