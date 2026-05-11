numbers = [4, 1, 7, 2, 7]

# Add Elements
numbers.append(10)
print(numbers)          # [4, 1, 7, 2, 7, 10]

numbers.insert(1, 99)
print(numbers)          # [4, 99, 1, 7, 2, 7, 10]

# Remove Elements
numbers.remove(7)       # removes first 7
print(numbers)          # [4, 99, 1, 2, 7, 10]

numbers.pop()           
print(numbers)          # [4, 99, 1, 2, 7]

numbers.pop(2)         #pops from index 2
print(numbers)          # [4, 99, 2, 7]

# Sorting
numbers.sort()
print(numbers)          # [2, 4, 7, 99]

numbers.sort(reverse=True)
print(numbers)          # [99, 7, 4, 2]

# Reverse
numbers.reverse()
print(numbers)          # [2, 4, 7, 99]

# Count
print(numbers.count(7)) # 1

# Find Index
print(numbers.index(99)) # 3

# Copy List
newList = numbers.copy()
print(newList)          # [2, 4, 7, 99]

# Clear List
newList.clear()
print(newList)          # []

# Extend List
a = [1, 2]
b = [3, 4]

a.extend(b)
print(a)                # [1, 2, 3, 4]