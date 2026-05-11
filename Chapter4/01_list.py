# Creating Lists
numbers = [1, 2, 3, 4, 5]
names = ["Aman", "Riya", "Kabir"]
mixed = [1, "Python", 3.5, True]

print(numbers)
print(names)
print(mixed)

# Indexing
print(numbers[0])      # 1
print(names[-1])       # Kabir

# Slicing
print(numbers[1:4])    # [2, 3, 4]

# Slicing with Skip
print(numbers[::2])    # [1, 3, 5]

# Reverse List
print(numbers[::-1])   # [5, 4, 3, 2, 1]

# Changing Values (Mutable)
numbers[0] = 100
print(numbers)

# Concatenation
a = [1, 2]
b = [3, 4]
print(a + b)           # [1, 2, 3, 4]

# Repetition
print(a * 3)           # [1, 2, 1, 2, 1, 2]

# Membership Operator
print(3 in numbers)    # True
print(10 in numbers)   # False

# Length
print(len(numbers))

# Nested Lists
nested = [[1, 2], [3, 4]]
print(nested[0])       # [1, 2]
print(nested[1][0])    # 3

# Looping Through List
for item in names:
    print(item)

# Empty List
empty = []
print(empty)