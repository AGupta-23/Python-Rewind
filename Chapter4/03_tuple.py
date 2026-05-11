# Creating Tuples
numbers = (1, 2, 3, 4, 5)
names = ("Aman", "Riya", "Kabir")
mixed = (1, "Python", 3.5, True)

print(numbers)          # (1, 2, 3, 4, 5)
print(names)            # ('Aman', 'Riya', 'Kabir')
print(mixed)            # (1, 'Python', 3.5, True)

# Single Element Tuple
single = (5,)
print(single)           # (5,)

# Indexing
print(numbers[0])       # 1
print(names[-1])        # Kabir

# Slicing
print(numbers[1:4])     # (2, 3, 4)

# Slicing with Skip
print(numbers[::2])     # (1, 3, 5)

# Reverse Tuple
print(numbers[::-1])    # (5, 4, 3, 2, 1)

# Concatenation
a = (1, 2)
b = (3, 4)

print(a + b)            # (1, 2, 3, 4)

# Repetition
print(a * 3)            # (1, 2, 1, 2, 1, 2)

# Membership Operator
print(3 in numbers)     # True
print(10 in numbers)    # False

# Length
print(len(numbers))     # 5

# Nested Tuples
nested = ((1, 2), (3, 4))

print(nested[0])        # (1, 2)
print(nested[1][0])     # 3

# Loop Through Tuple
for item in names:
    print(item)

# Immutability
# numbers[0] = 100 ❌ Error
# Tuples cannot be changed