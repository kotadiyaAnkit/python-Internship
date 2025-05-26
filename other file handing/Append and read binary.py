file_path = r"D:\python\other file handing\binary.txt"

# Open file in append+read binary mode
with open(file_path, "a+b") as file:
    # Append binary data
    file.write(b"\nNew appended binary data.")

    # Move to the start to read everything
    file.seek(0)
    content = file.read()

print("Binary file content:")
print(file)
print(content)
