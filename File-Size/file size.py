import os

file_info = os.stat("test_file.txt")
print file_info.st_size