# OPENING A FILE IN PYTHON

# Syntax:
# file_object = open("filename", "mode")

# Common modes:
# "r"  -> Read mode (default)
# "w"  -> Write mode (creates/overwrites file)
# "a"  -> Append mode
# "rb" -> Read binary file
# "rt" -> Read text file


# 1. OPEN FILE IN READ MODE
f = open("Chapter9/sample.txt", "r")

print(f)

f.close()   # Always close the file


# 2. OPEN FILE WITHOUT WRITING MODE
# "r" is default mode

f = open("Chapter9/sample.txt")

print(f)

f.close()


# 3. OPEN FILE IN WRITE MODE
# Creates file if not present
# Overwrites old content

f = open("Chapter9/sample.txt", "w")

f.close()


# 4. OPEN FILE IN APPEND MODE
# Adds content at end of file

f = open("Chapter9/sample.txt", "a")

f.close()


# 5. OPEN BINARY FILE
# Used for images, pdfs etc.

f = open("image.jpg", "rb")

print(f)

f.close()


# 6. CHECK FILE NAME AND MODE

f = open("Chapter9/sample.txt", "r")

print(f.name)   # Output: Chapter9/sample.txt
print(f.mode)   # Output: r

f.close()


# 7. USING WITH STATEMENT (BEST METHOD)
# Automatically closes file

with open("Chapter9/sample.txt", "r") as f:
    print(f)

# No need to write f.close()


# 8. OPEN FILE USING ABSOLUTE PATH

f = open("D:/PracticePython/Chapter9/sample.txt", "r")

print(f)

f.close()


# 9. FILE DOES NOT EXIST ERROR

# f = open("abc.txt", "r")
# Error -> FileNotFoundError

# Because file does not exist


# 10. CREATE NEW FILE USING WRITE MODE

f = open("newfile.txt", "w")

f.close()

print("File created")