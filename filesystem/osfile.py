import os

filename = "test.txt"

# Check file size and details
info = os.stat(filename)
print(info.st_size, "bytes")

# Delete the file
os.remove(filename)
print(filename, "has been deleted.")
