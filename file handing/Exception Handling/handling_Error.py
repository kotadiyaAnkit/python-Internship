try:
    file = open("D:\\WindowsApps", "r")
    content = file.read()
    print(content)
    file.close()
except IOError:
    print("An error occurred while reading the file!")