text = "python programming"

# Length
print(len(text))                 # 18

# Change Case
print(text.upper())              # PYTHON PROGRAMMING
print(text.lower())              # python programming
print(text.capitalize())         # Python programming
print(text.title())              # Python Programming

# Checking
print(text.startswith("py"))     # True
print(text.endswith("ing"))      # True

# Find & Count
print(text.find("pro"))          # 7
print(text.count("m"))           # 2

# Replace
print(text.replace("python", "java"))

# Remove Spaces
msg = "   hello   "
print(msg.strip())               # hello

# Split & Join
print(text.split())              # ['python', 'programming']

words = ['Python', 'is', 'fun']
print(" ".join(words))           # Python is fun

# String Checks
print("abc123".isalnum())        # True
print("Python".isalpha())        # True
print("123".isdigit())           # True

# Center
print(text.center(30, "-"))   #------python programming------
