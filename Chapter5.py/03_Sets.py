# Creating Sets
numbers = {1, 2, 3, 4}
print(numbers)          # {1, 2, 3, 4}

# Duplicate Values Removed
data = {1, 2, 2, 3, 3}
print(data)             # {1, 2, 3}

# Empty Set
empty = set()
print(type(empty))      # <class 'set'>

# Add Element
numbers.add(5)
print(numbers)          # {1, 2, 3, 4, 5}

# Remove Element
numbers.remove(2)
print(numbers)          # {1, 3, 4, 5}

# Discard Element
numbers.discard(10)     # No Error
print(numbers)

# Pop Random Element
numbers.pop()
print(numbers)

# Length
print(len(numbers))

# Membership
print(3 in numbers)     # True

# Looping
for item in numbers:
    print(item)