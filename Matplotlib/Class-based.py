from contextlib import contextmanager

@contextmanager
def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        yield file
    finally:
        file.close()
        print(f"{file_name} has been closed.")

# Using the custom context manager to write to the file
with open_file('Matplotib.txt', 'w') as f:
    f.write("Hello, world!")
