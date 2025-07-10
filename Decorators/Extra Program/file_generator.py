import os

def read_first_line(file_path):
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return  # Exit the function
    
    with open(file_path, 'r') as file:
        first_line = file.readline()  # Read ONLY the first line
        print(first_line)  # Print the first line

# Specify file path
file_path = 'D:\\python\\file handing\\mark.txt'

# Read and print the first line
read_first_line(file_path)


# def read_file_line_by_line(file_path):
#     with open(file_path, 'r') as file:
#         for line in file:
#             yield line.strip()  # Removes newline and extra spaces

# # Path to your file
# file_path = 'sample.txt'

# # Using the generator to read and print one line at a time
# for line in read_file_line_by_line(file_path):
#     print(f"Reading line: {line}")
