file_path = r"D:\\python\\other file handing\\read and write.txt"

# Binary content to write
binary_data = b'This is binary data.\nSecond line.'

# Write binary data to the file
with open(file_path, "wb") as f:
    f.write(binary_data)
    print(f)

print("Binary data written successfully.")
