# 4. Write a python program to print the contents of a directory using the os module. Search
# online for the function which does that.
# 5. Label the program written in problem 4 with comments.

import os

# Select directory path
path = "D:/PracticePython"

# Get list of files and folders
contents = os.listdir(path)    #-->>Function used is listdir()

# Print contents
print("Contents of directory:")

for item in contents:
    print(item)