name = "Abhidha"
surname = "Gupta"

# Indexing
print(name[0])          # A
print(surname[4])       # a

# Slicing
print(name[2:5])        # hid

# Slicing with Skip Value
print(name[0:7:2])      # Ahiha
print(name[::2])        # Ahiha
print(name[::-1])       # ahdihbA (reverse)

# Negative Indexing
print(name[-2:])        # ha

# String Operations
fullName = name + " " + surname
print(fullName)

# Length
print(len(name))        # 7

# Escape Sequence Characters
print("Hello\nWorld")
print("Hello\tWorld")

# Immutability
# name[0] = "R" ❌ Error (strings cannot be changed)

# Removing Spaces
text = "   Python   "
print(text.strip())     # Python