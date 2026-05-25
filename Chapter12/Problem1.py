# 1. Write a program to open three files 1.txt, 2.txt and 3.txt. If any of these files are not
# present, a message without exiting the program must be printed prompting the same.

try:
 with open("1.txt", "r") as f:
    print(f.read())
except Exception as v:
    print(v)

try:
 with open("1.txt", "r") as f:
    print(f.read())
except Exception as v:
    print(v)

try:
 with open("1.txt", "r") as f:
    print(f.read())
except Exception as v:
    print(v)

print("Program ended")
